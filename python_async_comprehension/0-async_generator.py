#!/usr/bin/env python3
"""this module contains a function async generator"""
from asyncio import sleep
from random import uniform
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    async generator that yields a random number
    between 0 and 10 after waiting for 1 second.

    Yields:
        int: A random number between 0 and 10.
    """
    for _ in range(10):
        await sleep(1)
        yield uniform(0, 10)
