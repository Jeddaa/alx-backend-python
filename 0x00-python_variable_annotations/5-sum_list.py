#!/usr/bin/env python3
'''task 5'''
from typing import List


def sum_list(input_list: List[float]) -> float:
    '''return the sum of a list passed in the function '''

    sun = 0.0
    for lis in input_list:
        sun += lis
    return sun
