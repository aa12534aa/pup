from fastapi import FastAPI
#a
app = FastAPI()

@app.get("/")
def hello():
    return {"message": "Hello World"}

@app.get("/add/{a}/{b}")
def add(a: int, b: int):
    return {"result": a + b}