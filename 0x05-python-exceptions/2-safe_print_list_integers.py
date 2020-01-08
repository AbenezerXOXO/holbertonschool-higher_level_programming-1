#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    index = 0
    while index < (x - 1):
        try:
            for i in range(index, x):
                print("{:d}".format(my_list[i]), end="")
                count += 1
            index = i
            print()
        except ValueError:
            index = i
            count -=1
    return count
