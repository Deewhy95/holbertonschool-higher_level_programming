#!/usr/bin/python3
""" class Rectangle that inherits from Base """

from models.base import Base


class Rectangle(Base):
    """
    Creates the class Rectangle that inherits from Base
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ class constructor """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
