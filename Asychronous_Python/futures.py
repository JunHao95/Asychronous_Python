import asyncio 
from results import fibo
async def main():
    future = asyncio.Future()
    await asyncio.ensure_future(fibo(future,10))
    print(future.result())

asyncio.run(main())
"""
Learning points

1) Define a future object
2) asyncio.ensure_future concerts fibo() corountine into a future object
3) print result of future using future.result
4) ensure_future() starts running the corountine which is passed as a parameter, as soon as the event loop is resumed
"""
