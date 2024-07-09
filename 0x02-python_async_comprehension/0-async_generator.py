#!/usr/bin/env python3
'''
async generator
'''
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    '''
    a coroutine that yields random number 0-10 10 times
    '''
    n = 0
    while n < 10:
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
        n += 1
