#!/usr/bin/python3
"""
This contains the inherits_from function
"""


def inherits_from(obj, a_class):
    """returns true if obj is an inst of a_class inherited, otherwise false"""
    return(issubclass(type(obj), a_class) and type(obj) != a_class)
