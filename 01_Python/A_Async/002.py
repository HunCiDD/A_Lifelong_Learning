# Future 对象
# Task 继承Future， Task内部 await结果的处理基于 Future 实现的

import asyncio


# 示例1
async def main():
    # 获取当前事件循环
    loop = asyncio.get_running_loop()
    # 创建一个Future对象，但什么也没有干
    fut = loop.create_future()
    # 等待任务的最终结果Future对象，没有结果则一直会等下去
    await fut

# 示例2

async def set_after(fut: asyncio.Future):
    await asyncio.sleep(2)
    # 给Future设置结果
    fut.set_result("666")


async def main2():
    # 获取当前事件循环
    loop = asyncio.get_running_loop()
    # 创建一个Future对象，但什么也没有干
    fut = loop.create_future()
    await loop.create_task(set_after(fut))

    data = await fut
    print(data)


if __name__ == "__main__":
    # asyncio.run(main())
    #   --->A、将main对应的协程对象，加入事件循环
    #   --->B、从事件循环中获取一个协程对象，即 main()协程对象，并运行其对应函数
    asyncio.run(main2())


