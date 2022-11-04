#!/usr/bin/python3
"""rectangle class"""
from models.base import Base


class Rectangle(Base):
    """The rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def height(self):
        """height getter function"""
        return self.__height

    @property
    def width(self):
        """width getter function"""
        return self.__width

    @property
    def x(self):
        """x getter function"""
        return self.__x

    @property
    def y(self):
        """y getter function"""
        return self.__y

    @height.setter
    def height(self, height):
        """height getter"""
        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @width.setter
    def width(self, width):
        """width setter"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @x.setter
    def x(self, x):
        """x setter"""
        if type(x) is not int:
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @y.setter
    def y(self, y):
        """y setter"""
        if type(y) is not int:
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y mustbe >= 0")
        self.__y = y

    def display(self):
        """public method display"""
        for i in range(self.height):
            print("#" * self.width)

    def area(self):
        """area method"""
        return self.width * self.height
