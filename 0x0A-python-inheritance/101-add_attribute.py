#!/usr/bin/python3
""" This module contains one function """


def add_attribute(obj, name, value):
    """
    adds a new attribute to an object if it’s possible
    """
    if obj.__class__.__module__ ==  '__builtin__':
        raise TypeError("can't add new attribute")
    else:
        obj.name = value
