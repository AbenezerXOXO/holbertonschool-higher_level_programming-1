#!/usr/bin/python3
""" This module contains one function """


def add_attribute(obj, name, value):
    """
    adds a new attribute to an object if it’s possible
    """
    if isinstance(obj, primitiveTypes):
        raise TypeError("can't add new attribute")
