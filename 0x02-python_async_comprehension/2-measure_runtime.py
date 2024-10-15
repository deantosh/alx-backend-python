#!/usr/bin/env python3
"""
Import async_comprehension from the previous file and write a
measure_runtime coroutine that will execute async_comprehension
four times in parallel using asyncio.gather.

measure_runtime should measure the total runtime and return it.

Notice that the total runtime is roughly 10 seconds, explain it
to yourself.
"""
import asyncio
from importlib import import_module
import time


async_comprehension = import_module(
    "1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """ Returns total runtime """

    # start time count
    start_time = time.perf_counter()

    await asyncio.gather(*(async_comprehension() for _ in range(4)))

    # stop time count
    stop_time = time.perf_counter()

    return stop_time - start_time
