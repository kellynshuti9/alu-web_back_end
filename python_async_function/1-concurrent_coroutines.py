#!/usr/bin/env python3
"""
This module runs multiple coroutines concurrently.
"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns wait_random n times with max_delay and returns
    the list of delays in ascending order.
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]

    results = []
    for task in asyncio.as_completed(tasks):
        result = await task
        results.append(result)

    return results
