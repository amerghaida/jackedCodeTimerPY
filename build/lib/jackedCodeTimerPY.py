import time
from tabulate import tabulate

try:
	from statistics import mean
except ImportError:
	def mean(values):
		return sum(values)/len(values)


class JackedTiming:
	def __init__(self):
		self.record = {}

	# starts the timer called label
	def start(self, label):
		try:
			self.record[label].start()
		except KeyError:
			self.record[label] = _Record()
			self.record[label].start()

	# stops the timer called label
	def stop(self, label):
		self.record[label].stop()

	# returns a string that contains the timing report that can be printed to the console.
	# highlight_labels can be a list or tuple that contains labels that will be highlighted in a seperate file so that they can be read more easily.
	def report(self, highlight_labels=None):
		if any(rec.started for rec in self.record.values()):
			raise JackedTimingError('Not all timers have been stopped.')

		tables = [sorted(self.record.items(), key=lambda a: sum(a[1].times), reverse=True)]
		if highlight_labels is not None:
			tables.insert(0, filter(lambda a: a[0] in highlight_labels, tables[0]))

		if highlight_labels: report_str = 'HIGHLIGHTS\n'
		else: report_str = ''
		for tbl in tables:
			report_str += tabulate(
					tuple((
							record[0],
							min(record[1].times),
							max(record[1].times),
							mean(record[1].times),
							sum(record[1].times),
							len(record[1].times)
						) for record in tbl),
					('label', 'min', 'max', 'mean', 'total', 'run count')
				)
			report_str += '\n\n'
		return report_str


class _Record:
	def __init__(self):
		self.started = False
		self.times = []

	def start(self):
		if self.started:
			raise JackedTimingError("Cannot have multiple instances of the same timer running simultaneously.")
		self.begin_time = time.time()
		self.started = True

	def stop(self):
		if not self.started:
			raise JackedTimingError("No start for this stop.")
		self.times.append(time.time() - self.begin_time)
		self.started = False


class JackedTimingError(BaseException):
	pass
