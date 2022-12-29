import asyncio


async def func():
    print('func begin')
    await asyncio.sleep(2)
    print('func end')
    return 'full filled !'

# create task 会将任务立即添加到事件循环里面
# task_list = [
#     asyncio.create_task(func(), name='task1'),
#     asyncio.create_task(func(), name='task2')
# ]

# 解决方法，向tasks里面放协程对象
task_list = [
    func(),
    func()
]

# asyncio 在内部会自动创建task，会在事件循环之后再创建task对象
done, pending = asyncio.run(asyncio.wait(task_list))
print(done)
