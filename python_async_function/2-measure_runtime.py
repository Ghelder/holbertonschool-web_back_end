#!/usr/bin/env python3
"""this module contains functions to measure the execution time"""

from time import time
from asyncio import run
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Calculates the average time it takes to run the
    `wait_n` function with a given number of iterations.

    Args:
        n (int): The number of iterations to
        run the `wait_n` function.
        max_delay (int): The maximum delay
        in seconds for each iteration of
        the `wait_n` function.

    Returns:
        float: The average time in seconds
        it takes to run the `wait_n`
        function for each iteration.
    """
    start_time = time()
    run(wait_n(n, max_delay))
    end_time = time()
    total_time = end_time - start_time
    return total_time / n
