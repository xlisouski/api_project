from fastapi import FastAPI
from app import routes  # <- Importa correctamente el módulo

app = FastAPI()

app.include_router(routes.router)