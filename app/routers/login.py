from fastapi import APIRouter, Depends, HTTPException
from app.models.userModel import UserLogin
from app.services.auth import create_token

router = APIRouter(
    prefix="/login",
    tags=["Login"]
)

@router.post(
    "",
    summary="Obter token para utilização da API",
    description="Retorna o JWT Token para utilizar nos requests da API"
)

def login(user: UserLogin):
    if user.username == "admin" and user.password == "123456":
        token = create_token(user.username)
        return {"access_token": token}
    raise HTTPException(status_code=401, detail="Credenciais inválidas")