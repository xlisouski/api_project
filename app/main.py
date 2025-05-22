from fastapi import FastAPI
from routes.hello import router  # IMPORTÁS el router directamente

app = FastAPI()

app.include_router(router)  # 

@app.get("/")
async def read_root():
    return {"message": "Hello World"}