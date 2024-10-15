import asyncio

async def task1():
    print("Task 1 started...")
    await asyncio.sleep(1)
    print("Task 1 completed.")
    return "Result 1"

async def task2():
    print("Task 2 started...")
    await asyncio.sleep(2)
    raise ValueError("Error in task 2!")

async def task3():
    print("Task 3 started...")
    await asyncio.sleep(1.5)
    print("Task 3 completed.")
    return "Result 3"


async def main():
    results = await asyncio.gather(
        task1(),
        task2(),
        task3(),
        return_exceptions=True
    )

    for idx, result in enumerate(results, start=1):
        if isinstance(result, Exception):
            print(f"Task {idx} raised an error: {result}")
        else:
            print(f"Task {idx} completed successfully: {result}")


asyncio.run(main())