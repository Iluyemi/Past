#!/usr/bin/python3
"""rectangle class"""
from models.base import Base


class Rectangle(Base):
    """The rectsangle class"""
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
        self.__height = height

    @width.setter
    def width(self, width):
        """width setter"""
        self.__width = width

    @x.setter
    def x(self, x):
        """x setter"""
        self.__x = x

    @y.setter
    def y(self, y):
        """y setter"""
        self.__y = y
