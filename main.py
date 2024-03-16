import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

# Had to add this code to make mirrord work
if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, log_level="info")
