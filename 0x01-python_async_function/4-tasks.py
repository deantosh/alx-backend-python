#!/usr/bin/env python3
"""
Take the code from wait_n and alter it into a new function task_wait_n.
The code is nearly identical to wait_n except task_wait_random is being
called.
"""
import asyncio
from typing import List
from importlib import import_module

task_wait_random = import_module("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int = 10) -> List[float]:
    """ Loop n times and wait for delay """
    tasks = [task_wait_random(max_delay) for i in range(n)]
    delays = []

    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays
