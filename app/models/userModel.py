from pydantic import BaseModel

class UserLogin(BaseModel):
    username: str
    password: str  # Apenas para demonstração, sem banco de dados real