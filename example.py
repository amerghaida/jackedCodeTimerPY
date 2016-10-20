from jackedCodeTimerPY import JackedTiming
JTimer = JackedTiming()

#amer testing 

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
  doSomethingHere = 'This is really useful'
  JTimer.stop('loop')


# measure function time
def someFunction():
  JTimer.start(someFunction)
  doSomethingHere = 'This is really useful'
  JTimer.stop(someFunction)
  return 'some value'

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
