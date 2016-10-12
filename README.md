# jackedCodeTimerPY
Simple but powerful code timer that can measure execution time of one line, functions, imports and gives statistics (min/max/mean/total time, number of executions).

![](https://github.com/BebeSparkelSparkel/jackedCodeTimerPY/blob/master/small.jpg?raw=true)

Get good data like this
```
label            min          max         mean        total    run count
-------  -----------  -----------  -----------  -----------  -----------
imports  0.00283813   0.00283813   0.00283813   0.00283813             1
loop     5.96046e-06  1.50204e-05  6.71864e-06  0.000335932           50
```

Install with pip
```shell
pip install git+git://github.com/BebeSparkelSparkel/jackedCodeTimerPY.git
pip3 install git+git://github.com/BebeSparkelSparkel/jackedCodeTimerPY.git
pip3.5 install git+git://github.com/BebeSparkelSparkel/jackedCodeTimerPY.git
```

### Import to your script
```python
from jackedCodeTimerPY import JackedTiming
JTimer = JackedTiming()
```

### Measure time and count calls
Measure loop times and count number of loops
```python
for i in range(50):
  JTimer.start('loop')
  doSomethingHere = 'This is really useful!'
  JTimer.stop('loop')
```

Measure function times an count the number of times the function is called
```python
def someFunction():
  JTimer.start(someFunction)
  doSomethingHere = 'This is really useful!'
  JTimer.stop(someFunction)
  return 'some value'
```

### Report Data
Get a well defined list with minimum, maximum, mean, and total times.
It also counts how many times the timer was run.
```python
JTimer.report()  # returns a string with the data table
print(JTimer.report())  # prints the data table

JTimer.report(['imports', 'loop'])  # includes a special highlights table with only timers 'imports' and 'loop'
```

### Example
[example](https://github.com/BebeSparkelSparkel/jackedCodeTimerPY/blob/master/example.py)
There is also a really good example [here](https://github.com/BebeSparkelSparkel/jackedCodeTimerPY/blob/master/example.py).

### Conclusion
I hope that jackedCodeTimerPY is super useful to you.
Let me know if you have any suggestions.
