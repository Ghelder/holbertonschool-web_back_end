#!/usr/bin/env python3
"""This module contains a function to calculate
the sum of a list of decimal numbers."""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """Calculates the sum of a list of decimal numbers.

    Args:
        input_list (List[float]): The list of
        decimal numbers to calculate the sum.

    Returns:
        float: The sum of the elements of input_list.
    """
    return sum(input_list)
