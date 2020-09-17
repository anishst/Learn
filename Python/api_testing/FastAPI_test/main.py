# https://fastapi.tiangolo.com/
# pip install fastapi
# pip install uvicorn - ASGI server, for production such as uvicorn

from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def read_root():
    return {"Hello": "World"}
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}



