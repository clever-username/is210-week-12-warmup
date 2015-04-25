#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 02 module"""


import datetime


class InvalidAgeError(Exception):
    """
    Custom exception class.
    """
    pass


def get_age(birthyear):
    """Function to calculate birthyear.

    args(int): Specified birthyear.

    returns:
        Valid, calculated age else error.
    Example:
        >>> get_age(2099)
        Traceback (most recent call last):
        File "<stdin>", line 1, in <module>
        __main__.InvalidAgeError
    """
    age = datetime.datetime.now().year - birthyear

    if age >= 0:
        return age
    else:
        raise InvalidAgeError
