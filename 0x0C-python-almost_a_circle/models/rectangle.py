#!/usr/bin/python3
""" class Rectangle that inherits from Base
"""

from models.base import Base


class Rectangle(Base):
    """ class Rectangle """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ class constructor """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ setter, validations """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ getter """
        return self.__height

    @height.setter
    def height(self, value):
        """ setter, validations """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ getter """
        return self.__x

    @x.setter
    def x(self, value):
        """ setter, validations """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ getter """
        return self.__y

    @y.setter
    def y(self, value):
        """ setter, validations """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ public method that returns the area value of the Rectangle """
        return (self.width * self.height)

    def display(self):
        """ Adding the public method that prints
        the Rectangle with the character # """
        if self.y != 0:
            print('\n'*self.y, end='')
        for index in range(self.height):
            print('{}{}'.format(' '*self.x, '#'*self.width))

    def __str__(self):
        """ method """
        return("[Rectangle] ({}) {}/{} - {}/{}").format(
            self.id, self.x, self.y, self.width, self.height)

    def update(self, *args):
        """ Public method that assigns an argument to each attribute """
        if len(args) == 1:
            return self.id
        elif len(args) > 1:
            return self.width
