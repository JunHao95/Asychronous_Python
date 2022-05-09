import asyncio

async def main():
    result = await.asyncio.gather(
            fibo("A",-1),
            fibo("B",-1),
            fibo("C",-1),
            fibo("D",-1),
            fibo("E",-1),
            return_exceptions=True
            )

    print(result)

