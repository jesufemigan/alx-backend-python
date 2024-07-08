#!/usr/bin/env python3

'''
basic async file
'''
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    '''A coroutine using asyncio and random module'''
    random_delay = random.uniform(0, max_delay)
    await asyncio.sleep(random_delay)
    return random_delay
