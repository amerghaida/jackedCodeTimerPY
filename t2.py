from jackedCodeTimerPY import JackedTiming
JTimer = JackedTiming()

word = {"success":0, "desire":0, "effort":0}
def cleaner(x):
    dust = ",./<>?;''[]{}\=+_)(*&^%$#@!`~"
    for letter in x:
        if letter in dust:
            x = x[0:x.index(letter)]+x[x.index(letter)+1:]
        else:
            pass
    return x #alhamdlillah it worked 31.07.12
print "input text to analyze"
itext = cleaner(raw_input()).split()

# t = time.clock()
JTimer.start('timer_1')
for iword in itext:
    if iword in word:
        word[iword] += 1
    else:
        pass
# print t
JTimer.stop('timer_1')
print JTimer.report()
print len(itext)