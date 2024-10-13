#!/usr/bin/env python3
"""
Write a type-annotated function floor which takes a float n as argument
and returns the floor of the float.
"""
import math


def floor(n: float) -> int:
    """ Returns: floor of a floating number """
    return int(math.floor(n))
