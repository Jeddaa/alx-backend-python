#!/usr/bin/env python3
'''task 6'''

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int | float]]) -> float:
    '''return the sum of the list passed into the function'''

    sun = 0.0
    for lis in mxd_lst:
        sun += lis

    return sun
