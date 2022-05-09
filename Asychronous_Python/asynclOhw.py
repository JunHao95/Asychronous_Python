#Asyncio.sleep suspends the current task but enables all other tasks to operate

import asyncio
async def main():
    print("Hello...")
    await asyncio.sleep(1)
    print("....World!")
asyncio.run(main())
