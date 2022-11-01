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
