#!/usr/bin/python3
""" class Square that inherits from Rectangle """

from models.rectangle import Rectangle


class Square(Rectangle):
    """ class Square """

    def __init__(self, size, x=0, y=0, id=None):
        """ class constructor """
        super().__init__(size, size, x, y)

    def __str__(self):
        """ __str__ method """
        return ('[Square] ({}) {}/{} - {}').format(
            self.id, self.x, self.y, self.width)
