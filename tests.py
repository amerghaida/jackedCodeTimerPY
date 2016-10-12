import unittest

from jackedCodeTimerPY import JackedTiming, _Record, JackedTimingError

class TestCodeTimer(unittest.TestCase):
  def test__Record(self):
    record = _Record()

    record.start()
    self.assertTrue(record.started)
    record.stop()
    self.assertFalse(record.started)
    self.assertTrue(len(record.times) == 1)
    self.assertTrue(record.times[0] > 0)

    record.start()
    with self.assertRaises(JackedTimingError):
      record.start()
    record.stop()
    self.assertTrue(len(record.times) == 2)
    self.assertTrue(record.times[1] > 0)

    with self.assertRaises(JackedTimingError):
      record.stop()

  def test_JackedTiming(self):
    timers = JackedTiming()

    timers.start('first')
    timers.start(_Record)

    with self.assertRaises(JackedTimingError):
      timers.start('first')
    timers.stop('first')
    with self.assertRaises(JackedTimingError):
      timers.stop('first')

    with self.assertRaises(JackedTimingError):
      timers.report()

    timers.stop(_Record)
    timers.report()
    timers.report(('first', 'second'))



if __name__ == '__main__': unittest.main()
