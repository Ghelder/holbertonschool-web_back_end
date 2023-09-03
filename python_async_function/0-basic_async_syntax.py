#!/usr/bin/env python3
"""definite function async that returns a random number float"""
from random import uniform
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """wait for a random delay in seconds"""
    delay = uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
