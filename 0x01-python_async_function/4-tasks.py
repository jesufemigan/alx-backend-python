#!/usr/bin/env python3
'''
tasks Task 4
'''


import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''function that runs multiple coroutines'''
    new_list = []
    while (n > 0):
        time = await task_wait_random(max_delay)
        new_list.append(time)
        await asyncio.sleep(time)
        n -= 1
    return sorted(new_list)
