#!/usr/bin/python3
"""This module provides a function for
calculating the length of elements in a list"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Calculate the length of each element
    in the given list and return a new list
    of tuples containing the element and its length.

    Args:
        lst (Iterable[Sequence]): The list
        or iterable of sequences.

    Returns:
        List[Tuple[Sequence, int]]:
        The list of tuples, where each
        tuple contains the element from
        the original list and its
        corresponding length.
    """
    return [(i, len(i)) for i in lst]
