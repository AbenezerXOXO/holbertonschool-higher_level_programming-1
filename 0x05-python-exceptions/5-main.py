#!/usr/bin/python3
raise_exception = __import__('5-raise_exception').raise_exception

try:
    num = int(input('give a number different to 0 = '))
    if num == 0:
        raise_exception()
    else:
        print("congrats")
except TypeError:
    print("Exception raised")
