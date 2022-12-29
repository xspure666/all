# 安装插件
# pip install fastapi -i https://mirrors.aliyun.com/pypi/simple
# pip install uvicorn -i https://mirrors.aliyun.com/pypi/simple
# 启动程序：uvicorn main:app -reload [main=main.py, app：app=FastAPI]
from fastapi import FastAPI
import time
from enum import Enum

app = FastAPI()


# 限制请求的类型
class lmt(str, Enum):
    Name = "lmt"
    Year = 32
    Id = "202222222"
    student = False


@app.get("/lmt/abcd/{hello}")
def lmt1(hello: lmt):  # 调用限制的类型
    return {'status': hello}


@app.get("/hello/{info}")
async def HelloWord():
    timestamp = str(time.time())
    return str('当前时间为：' + timestamp)


@app.post("/update/{info}")
async def update_info(info):
    return f"update info sucessful {info}"


@app.get("/lmt/{item_name}")
def lmt_1(item_name: str):
    a = 100 + 200
    return str(a)


@app.get('/add/')
def add(num1: int = 100, num2: int = 90):
    return {f'num1 + num2 = {num1 + num2}'}
