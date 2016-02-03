from __future__ import division
i = 1

while i < 50:
    if i%3 == 0 and i%5 == 0:
        print "FizzBuzz", i
    elif i%3 == 0:
        print "Fizz", i
    elif i%5 == 0:
        print "Buzz", i
    else:
        print "nope", i
    i = i + 1
print "done"
