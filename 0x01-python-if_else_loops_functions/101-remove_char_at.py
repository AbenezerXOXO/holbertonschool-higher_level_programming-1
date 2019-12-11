#!/usr/bin/python3
def remove_char_at(str, n):
    for i in str:
        if i != n:
            copy[i] = str[i]
        else:
            i = i + 1
