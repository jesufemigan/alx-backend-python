#!/usr/bin/env python3
'''
execute multiple coroutines at the same time with async
'''
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''function that runs multiple coroutines'''
    new_list = []
    while (n > 0):
        time = await wait_random(max_delay)
        new_list.append(time)
        await asyncio.sleep(time)
        n -= 1
    return sorted(new_list)
