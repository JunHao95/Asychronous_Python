import asyncio
import random

async def this_is_a_task():
    print("Task execution")
    temp = random.randint(0,100)
    return temp

async def main():
    for i in range(0,5):
        task = asyncio.create_task(this_is_a_task())
        await task
        print(task.result())

asyncio.run(main())
