from pydantic import BaseModel

class User(BaseModel):
    nombre: str
    edad: int