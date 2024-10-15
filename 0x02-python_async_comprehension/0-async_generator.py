#!/usr/bin/env python3
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    '''
    this coroutine randomly generate number from 0
    to 10 in an asynchronous manner

    '''
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
