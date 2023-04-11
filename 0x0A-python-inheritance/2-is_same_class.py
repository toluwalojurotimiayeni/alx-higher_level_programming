#!/usr/bin/python3
"""
This contains the function is_same_class
"""


def is_same_class(obj, a_class):
    """This returns true if obj is the exact class a_class, otherwise false"""
    return (type(obj) == a_class)
