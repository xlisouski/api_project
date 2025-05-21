from fastapi import FastAPI
from app.routes import hello  # Esto requiere que exista app/routes.py

app = FastAPI()

app.include_router(hello.router)

@app.get("/")
async def read_root():
    return {"message": "Hello World"}

@app.get("/hello")
async def read_hello():
    return hello()