import asyncio

async def main():
    test()


asyncio.create_task(test())
await test()

