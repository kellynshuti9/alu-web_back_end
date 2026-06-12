#!/usr/bin/env python3
""" Asynchronous coroutine """
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """ Asynchronous coroutine that waits for a random delay
    between 0 and max_delay (included and float value)
    seconds and returns it.
    """

    random_val = random.uniform(0, max_delay)
    await asyncio.sleep(random_val)
    return random_val
