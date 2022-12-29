#!/usr/bin/env python3

import asyncio
import time
import random


async def foo1():
    return await asyncio.sleep(random.randint(1, 10) / 100.0), \
           print(f"foo1耗时{time.time() - start}")


async def foo2():
    return await asyncio.sleep(random.randint(1, 10) / 100.0), \
           print(f"foo2耗时{time.time() - start}")


async def foo3():
    return await asyncio.sleep(random.randint(1, 10) / 100.0), \
           print(f"foo3耗时{time.time() - start}")


async def foo4():
    return await asyncio.sleep(random.randint(1, 10) / 100.0), \
           print(f"foo4耗时{time.time() - start}")


async def main():
    await asyncio.gather(foo1(), foo2(), foo3(), foo4())


if __name__ == "__main__":
    start = time.time()
    asyncio.run(main())
