# -*- coding:utf-8 -*-
import asyncio
import aiofiles
import time


# 异步操作时，函数名前必须加上async
async def func1():
    # 异步写入文件
    async with aiofiles.open("text.txt", "a", encoding="utf-8") as f:
        await f.write("hello func1!\n")
        print("func1数据写入成功")


async def func2():
    async with aiofiles.open("text.txt", "a", encoding="utf-8") as f:
        await f.write("hello func2!\n")
        await func1()
        print("func2数据写入成功")


# 把多个任务加入列表，注意：调用协程函数时，函数内部代码不会执行，只是会返回一个协程对象。
async def main():
    tasks = [
        func1(),
        func2()
    ]
    await asyncio.wait(tasks)


if __name__ == "__main__":
    t1 = time.time()
    asyncio.run(main())
    t2 = time.time()
    print(t2 - t1)
