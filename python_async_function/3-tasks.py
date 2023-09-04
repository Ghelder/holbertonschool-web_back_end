#!/usr/bin/env python3
"""This module provides a function for creating an asyncio.Task"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Creates an asyncio.Task object that waits
    for a random period of time.

    Args:
        max_delay (int): The maximum delay in
        seconds for the random wait period.

    Returns:
        asyncio.Task: The created task that
        waits for a random period of time.
    """
    return asyncio.create_task(wait_random(max_delay))
