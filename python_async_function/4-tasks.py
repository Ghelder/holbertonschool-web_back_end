#!/usr/bin/env python3
"""This module provides functions for performing async operations with random delays."""
from asyncio import gather
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns `task_wait_random` `n` times with the specified `max_delay`.

    Args:
        n (int): The number of times to spawn `task_wait_random`.
        max_delay (int): The maximum delay for each `task_wait_random` call.

    Returns:
        List[float]: The list of delays in ascending order.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = await gather(*tasks)
    return sorted(delays)
