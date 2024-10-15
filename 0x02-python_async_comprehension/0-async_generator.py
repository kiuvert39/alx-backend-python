#!/usr/bin/env python3
import asyncio
import random
from typing import Generator


async def async_generator():
    '''
    this coroutine randomly generate number from 0
    to 10 in an asynchronous manner

    '''
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
