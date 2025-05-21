from fastapi import FastAPI
from app.routes.hello import router  # IMPORTÁS el router directamente

app = FastAPI()

app.include_router(router)  # Y lo incluís acá

@app.get("/")
async def read_root():
    return {"message": "Hello World"}