#!/usr/bin/python3
""" class Rectangle that inherits from Base """


from models.base import Base


class Rectangle(Base):
    """ class Rectangle """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ class constructor """

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)
