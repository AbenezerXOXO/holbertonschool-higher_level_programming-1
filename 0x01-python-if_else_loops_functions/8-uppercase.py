#!/usr/bin/python3
def uppercase(str):
    for i in range(str):
        if ord(i) >= 97 and ord(i) <= 122:
            l = ord(i - 32)
        else:
            l = i
        print("{:c}".format(l), end="")
    print("\n")
