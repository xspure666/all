import uvicorn
from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@app.get("/items/")
async def read_items(token: str = Depends(oauth2_scheme)):
    return {"token": token}


if __name__ == '__main__':
    uvicorn.run(app="demo1:app", reload=True, host="127.0.0.1", port=8080)
