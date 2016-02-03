from __future__ import division

def celsius(number):
    c = (number - 32) * 5/9
    return "{} degrees F is {} Celsius". format(number, c)

def fahrenheit(number):
    f = number *9/5 + 32
    return "{} degrees C is {} fahrenheit". format(number, f)


print fahrenheit(37)
    
print celsius(72)
