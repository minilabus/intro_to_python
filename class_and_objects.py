#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Short example on object and class manipulation.
See detail here: https://www.freecodecamp.org/news/python-property-decorator/
"""


class Person():
    """ Class for representing a person

    Attributes
    ----------
    eye_color : string
        The color of person's eyes
    nb_eyes : int
        The number of eyes of the person

    Methods
    -------
    __len__()
        Returns the number of eyes of the person
    __str__()
        Returns a string representation of the person
    """

    def __init__(self, eye_color, nb_eyes=2):
        """ Constructor for the Person class
        Parameters
        ----------
        eye_color : string
            The color of person's eyes
        nb_eyes : int, optional
            The number of eyes of the person, default to 2
        """
        # This will use the setter function below
        self.eye_color = eye_color
        self.nb_eyes = nb_eyes
        # This will NOT use the setter function below
        # self._eye_color = eye_color
        # self._nb_eyes = nb_eyes

    def __len__(self):
        """ Returns the number of eyes of a person """
        return self.nb_eyes

    def __str__(self):
        """ Returns a string representation of a person with their eye color
        and number of eyes
        """
        return 'This person has {} {} eyes.'.format(self.nb_eyes,
                                                    self.eye_color)

    @property
    def eye_color(self):
        """ Returns the eye color of a person """
        return self._eye_color

    @eye_color.setter
    def eye_color(self, eye_color):
        """ Set the eye color of a person """
        if not isinstance(eye_color, str):
            raise ValueError('Invalid value for eye_color (not string)!')
        self._eye_color = eye_color

    @property
    def nb_eyes(self):
        """ Returns the number of eyes of a person """
        return self._nb_eyes

    @nb_eyes.setter
    def nb_eyes(self, nb_eyes):
        """ Set the number of eyes of a person """

        if not isinstance(nb_eyes, int):
            raise ValueError('Invalid value for nb_eyes (not integer)!')
        self._nb_eyes = nb_eyes


person_1 = Person('green', 2)
person_2 = Person('blue', 1)

print(person_1)
print(len(person_1), person_1.eye_color, person_1.nb_eyes)
# person_3 = Person(['black'], 2)
# person_3 = Person('black', 2.0)
