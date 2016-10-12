import time
from statistics import mean
from tabulate import tabulate


class CodeTiming:
	def __init__(self):
		self.record = {}

	def start(self, label):
		try:
			self.record[label].start()
		except KeyError:
			self.record[label] = _Record()
			self.record[label].start()

	def end(self, label):
		self.record[label].end()

	# def time_process(self, label, process):
	# 	self.start(label)

	def report(self, show_labels=None):
		tables = [sorted(self.record.items(), key=lambda a: sum(a[1].times), reverse=True)]
		if show_labels is not None:
			tables.insert(0, filter(lambda a: a[0] in show_labels, tables[0]))

		for tbl in tables:
			print(
				tabulate(
					tuple((record[0], min(record[1].times), max(record[1].times), mean(record[1].times), sum(record[1].times), len(record[1].times))
						for record in tbl
					),
					('label', 'min', 'max', 'mean', 'total', 'run count')
				)
			)


class _Record:
	def __init__(self):
		self.started = False
		self.times = []

	def start(self):
		if self.started:
			raise CodeTimingError("Cannot have multiple instances of the same timer running simultaneously.")
		self.begin_time = time.time()
		self.started = True

	def end(self):
		if not self.started:
			raise CodeTimingError("No start for this end.")
		self.times.append(time.time() - self.begin_time)
		self.started = False


class CodeTimingError(BaseException):
	pass
