#!/usr/bin/env python3
"""This module provides a function for
creating multiplier functions"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Create and return a function that
    multiplies a float by the given multiplier.

    Args:
        multiplier (float): The multiplier to be used.

    Returns:
        Callable[[float], float]: A function that accepts
        a float and returns the result of multiplying it
        by the multiplier.
    """

    def multiply_by_float(number: float) -> float:
        """Multiply a given number by a float value.

        Args:
            number (float): The number
            to be multiplied.

        Returns:
            float: The result of multiplying the
            number by the multiplier.
        """
        return number * multiplier

    return multiply_by_float
