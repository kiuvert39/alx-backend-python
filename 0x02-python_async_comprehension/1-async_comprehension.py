async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    """Coroutine that collects 10 random
    numbers using async comprehension.
    """

    random = [num async for num in async_generator()]
    return random
