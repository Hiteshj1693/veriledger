from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello, World!!"}

@app.get("/root-path")
async def read_root_path():
    return {"message": "Hello, Root Path!!"}