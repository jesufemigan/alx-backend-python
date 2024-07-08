#!/usr/bin/env python3
'''
measure the runtime
'''

import time
import asyncio


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    '''
    measures the runtime
    '''
    time_start = time.time()
    asyncio.run(wait_n(n, max_delay))
    return (time.time() - time_start) / n
