from fastapi import FastAPI
from app.routes import hello  # Esto requiere que exista app/routes.py

app = FastAPI()

app.include_router(hello.router)