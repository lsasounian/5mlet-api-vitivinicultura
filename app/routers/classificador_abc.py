from fastapi import APIRouter, Depends, Query
from app.services.auth import verify_token
from app.services.classificador_abc import exportacao_abc

router = APIRouter(
    prefix="/abc_exportacao",
    tags=["Exportação ABC"],
    dependencies=[Depends(verify_token)]
)

@router.get(
    "",
    summary="Classificador ABC",
    description="Retorna os dados de Classificador ABC"
)

def get_abc_exportacao(dados: str = Query(None)):
    return exportacao_abc(dados)