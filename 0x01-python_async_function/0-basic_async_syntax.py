import asyncio

async def download_data(source, delay):
     print(f"Starting download from {source}...")

     await asyncio.sleep(delay)

     print(f"Finished downloading from {source} in {delay} seconds.")
     return f"Data from {source}"


async def main():
    task1 = asyncio.create_task(download_data('Source 1', 3))
    task2 = asyncio.create_task(download_data('Source 2', 2))

    data1, data2  = await asyncio.gather(task1, task2)

    print(data1)
    print(data2)

asyncio.run(main())