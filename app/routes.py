from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def read_root():
    return {"mensaje": "¡Bienvenida a tu API, Ximena!"}

@router.get("/saludo/{nombre}")
def saludar(nombre: str):
    return {"saludo": f"Hola, {nombre}!"}