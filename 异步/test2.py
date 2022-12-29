import asyncio


import asyncio

async def func1():
    print("start")
    await func2()     # 等待协程对象
    await func3()
    print("end")


async def func2():
    i = 0
    while True:
        if i < 10:
            await asyncio.sleep(1)
            print(i)
            i += 1
        else:
            break

async def func3():
    i = 10
    while True:
        if i < 20:
            await asyncio.sleep(1)
            print(i)
            i += 1
        else:
            break

asyncio.run(func1())
