#!/usr/bin/env python3
"""This module provides a function for calculating
the sum of a list of integers and floats."""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Calculates the sum of a list of integers and floats.

    Args:
        mxd_lst (List[Union[int, float]]): The list of
        integers and floats to calculate the sum.

    Returns:
        float: The sum of the elements of mxd_lst.
    """
    return sum(mxd_lst)
