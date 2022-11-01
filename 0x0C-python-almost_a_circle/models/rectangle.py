#!/usr/bin/python3
"""My rectangle class"""
from models.base import Base


class Rectangle(Base):
	"""inheriting from base class"""


	def __init__(self, width, height, x=0, y=0, id=None):
		"""initialization function"""
		self.width = width
		self.height = height 
		self.x = x
		self.y = y
		super().__init__(id)
	@property
	def height(self):
		"""getter for height"""
		return(self.__height)
	@property
	def width(self):
		"""getter for height"""
                return(self.__width)
	@property
	def x(self):
		"""getter for x"""
		return(self.__x)
	@property
	def y(self):
		 """getter for y"""
		return(self.__y)
	@height.setter
	def height(self, value):
		""" setter for height"""
		self.__value = value
	def width(self, value):
		"""setter for width"""
		self.__value = value
	
