#!/bin/bash/python3
"""square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """initialization from inheritance"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """string for square"""
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x,
                                                 self.y,
                                                 self.width
                                                 )

    @property
    def size(self):
        """size getter"""
        return self.height

    @size.setter
    def size(self, size):
        """size setter"""
        self.width = size
        self.height = size
