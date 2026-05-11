#!/usr/bin/env python3
"""
Measures runtime of async comprehensions.
"""

import asyncio
import time
from typing import Callable

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Runs async_comprehension 4 times in parallel and
    returns total execution time.
    """
    start = time.time()

    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )

    end = time.time()

    return end - start
