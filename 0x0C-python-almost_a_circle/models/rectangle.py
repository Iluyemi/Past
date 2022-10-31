#!/usr/bin/python3

from models.base import Base

if __name__ == "__main__":
    class Rectangle(Base):
        def __init__(self, width, height, x=0, y=0, id=None):
            Base.__init__(self, id)
            self.__height = height 
            self.__width = width 
            self.__x = x 
            self.__y = y
