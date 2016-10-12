from jackedCodeTimerPY import JackedTiming
JTimer = JackedTiming()

JTimer.start('imports')  # measures the time to import packages
import numbers
import math
import cmath
import decimal
import fractions
import random
import statistics
import itertools
import functools
import operator
JTimer.stop('imports')

# measure and count loops
for i in range(50):
  JTimer.start('loop')
  sorted((1,1234,51,5,124,1234,34,65,2345,123,4,12,412,3,145,345,12,341,23,23645,3245,12,34,123,56,32,5,1234,1234,4,1235,3245,2,345,2345,1,234,1234,123,45,3214,1243,1235,4))
  JTimer.stop('loop')

# measure function time
def someFunction():
  JTimer.start(someFunction)
  doSomethingHere = 'This is really useful!'
  JTimer.stop(someFunction)
for i in range(10): someFunction()


print(JTimer.report(['imports', 'loop']))
'''
HIGHLIGHTS
label            min          max         mean        total    run count
-------  -----------  -----------  -----------  -----------  -----------
imports  0.00283813   0.00283813   0.00283813   0.00283813             1
loop     5.96046e-06  1.50204e-05  6.71864e-06  0.000335932           50

label                                           min          max         mean        total    run count
--------------------------------------  -----------  -----------  -----------  -----------  -----------
imports                                 0.00283813   0.00283813   0.00283813   0.00283813             1
loop                                    5.96046e-06  1.50204e-05  6.71864e-06  0.000335932           50
<function someFunction at 0x101256f28>  9.53674e-07  2.14577e-06  1.19209e-06  1.19209e-05           10
'''
