#!/usr/bin/env python3
"""
Import wait_random from the previous python file that you’ve written
and write an async routine called wait_n that takes in 2 int arguments
(in this order): n and max_delay. You will spawn wait_random n times
with the specified max_delay.

wait_n should return the list of all the delays (float values).
The list of the delays should be in ascending order without using sort()
because of concurrency.
"""
import importlib
import asyncio
from typing import List


wait_random = importlib.import_module("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """ Loop n times and wait for delay """
    tasks = [asyncio.create_task(wait_random(max_delay)) for i in range(n)]
    delays = []

    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays
