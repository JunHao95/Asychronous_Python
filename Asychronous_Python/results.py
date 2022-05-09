#Processing multiple values :  Create multiple corountine and collect return values

import asyncio 

async def fibo(value):
    if value < 0 :
        raise "Negative number"

    a,b = 0,1
    for i in range(2,value+1):
        a,b = b , a+b

    return b

async def runner(values):
    requests = [asyncio.create_task(fibo(number)) for number in values]
    done , pending = await asyncio.wait(requests)
    results = [res.result() for res in done]
    print("Total results: {}".format(len(results)))
    print("pending results: {}".format(len(pending)))
    print(sorted(results))



if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(runner([1,10,2,3,4,15,6]))
    loop.close()

"""
Learning points
1) use of event loop for processing via asyncio.get_event_loop()
2)use run_until_complete() to excute the required amount of unners that are going to perform the desired jobs
3) Go to the runner() corountine, executes the required number of fibo() corountines and collects the result
4) parameter of asyncio.wait() is teh list of corountines that are about to get executed , return values of asyncio.wait() are two futures
"""

