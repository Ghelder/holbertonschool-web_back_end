#!/usr/bin/env python3
"""This module contains functions asyncs"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns `wait_random` `n` times with the specified `max_delay`.

    Args:
        n (int): The number of times to spawn `wait_random`.
        max_delay (int): The maximum delay for each `wait_random` call.

    Returns:
        List[float]: The list of delays in ascending order.
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
