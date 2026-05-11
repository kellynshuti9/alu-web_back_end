#!/usr/bin/env python3
"""
This module runs multiple asyncio tasks concurrently.
"""

import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns task_wait_random n times and returns sorted delays.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]

    results = []
    for task in asyncio.as_completed(tasks):
        results.append(await task)

    return results
