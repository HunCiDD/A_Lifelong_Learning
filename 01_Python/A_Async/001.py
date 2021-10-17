# 事件循环---理解为一个死循环，去检测并执行某些代码


# 伪代码描述
"""
任务列表 = [任务1， 任务2， 任务3]

while True：
    就绪的任务列表 = 去任务列表中检测所有的任务状态
    已完成的任务列表 = 去任务列表中检测所有的任务状态

    for 任务 in 可执行的任务列表:
        执行就绪任务

    for 任务 in 已完成的任务列表：
        在任务列表中移除

    如果任务列表为空，退出循环
"""
import asyncio


# 协程函数，使用async def 定义的函数
async def func():
    pass

# 协程对象, 协程函数()的返回值
result = func()

# 生成获取一个事件循环
loop = asyncio.get_event_loop()
# 将任务放到任务列表
loop.run_until_complete(result)
# asyncio.run(result) 3.7

# await + 可以等待的对象（协程对象、Future、Task对象-> IO等待）
# await 就是等待后面有结果之后，程序才跳回来继续执行函数


# Task，帮助在事件循环中添加任务
# Tasks用于并发调度协程，通过asyncio.create_task(协程对象)的方式创建Task对象，这样
# 可以让协程加入事件循环中，等待被调度执行。除了使用asyncio.create_task()函数外，还
# 可以使用低层的loop_create_task() 或 ensure_future() 函数。不建议手动实例化Task对象。

# 示例1
async def func():
    print(1)
    await asyncio.sleep(2)
    print(2)
    return "返回值"


async def main1():
    print("main开始")
    # 创建Task对象，将Task加入事件循环
    task1 = asyncio.create_task(func())
    task2 = asyncio.create_task(func())
    print("main结束")
    ret1 = await task1
    ret2 = await task2
    print(ret1, ret2)


async def main2():
    # 方式二、写法
    print("main开始")
    tasks = [
        asyncio.create_task(func()),
        asyncio.create_task(func())
    ]
    done, pa = asyncio.wait(tasks)
    print("main结束")
    print(done)


if __name__ == "__main__":
    asyncio.run(main1())
