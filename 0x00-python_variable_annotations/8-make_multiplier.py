#!/usr/bin/env python3
''' task 8 '''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''return a function '''

    def new_func(multiplier: float):
        '''return a float multipied by the multiplier '''

        return 10.0 * multiplier
    return new_func
