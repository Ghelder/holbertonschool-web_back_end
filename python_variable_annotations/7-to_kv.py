#!/usr/bin/env python3
"""This module provides a function for creating a tuple with
a string key and the square of an integer or float value."""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Creates a tuple with the string k as the first
    element and the square of v as the second element.

    Args:
        k (str): The string element.
        v (Union[int, float]): The integer or float element.

    Returns:
        Tuple[str, float]: A tuple with k as the first
        element and the square of v as the second element.
    """
    return k, v**2
