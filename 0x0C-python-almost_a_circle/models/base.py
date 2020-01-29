#!/usr/bin/python3
""" Base """
import json


class Base:
    """
    Class 'Base' will be the “base” of all other classes
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ class constructor """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ JSON string representation """
        if list_dictionaries is None or len(list_dictionaries) is 0:
            return "[]"
        else:
            return(json.dumps(list_dictionaries))
