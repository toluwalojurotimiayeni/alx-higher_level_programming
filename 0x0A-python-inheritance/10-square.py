#!/usr/bin/python3
"""
This inherits from Rectangle and contains the class BaseGeometry
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A representation of a square"""
    def __init__(self, size):
        """The instantiation of the square"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """"This returns the area of the square"""
        return self.__size ** 2
