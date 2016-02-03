#from __future__ import division
#print "1+1=",1+1
#print "5/2=",5/2

base = raw_input('What is the base?')

exponent = raw_input('What is the exponent?')

answer = float(base) ** float(exponent)

print "{} to the power of {} = {}". format(base,exponent, answer)
