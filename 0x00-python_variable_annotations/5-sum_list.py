#!/usr/bin/env python3
"""
Write a type-annotated function sum_list which takes a list input_list of
floats as argument and returns their sum as a float.
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """ Returns: a sum of a list of floats """
    total = 0.0
    for num in input_list:
        total += num
    return total
