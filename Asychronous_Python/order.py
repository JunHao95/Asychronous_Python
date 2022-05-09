
import asyncio
import random

async def task_corountine(pid):
    await asyncio.sleep(random.randint(0,2))
    print("Task %s done"%pid)

async def concurrently():
    tasks = [task_corountine(i) for i in range(1,10)]
    await asyncio.gather(*tasks)
asyncio.run(concurrently())

#key pointers
"""
1)created a corountine that sleeps for a random amount of time
2) Definite of second corountine named concurrently() that generates 10 task_corountine()
3) results collected using asyncio.gather
4) Execution of concurrently() using asyncio.run() 

"""
