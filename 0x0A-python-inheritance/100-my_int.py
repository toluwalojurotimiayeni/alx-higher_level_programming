#!/usr/bin/python3
"""
This contains the class MyInt
"""


class MyInt(int):
    """This is a rebel"""
    def __new__(cls, *args, **kwargs):
        """This create a new instance of the class"""
        return super(MyInt, cls).__new__(cls, *args, **kwargs)

    def __eq__(self, other):
        """what was != is now =="""
        return int(self) != other

    def __ne__(self, other):
        """what was == is now !="""
        return int(self) == other
