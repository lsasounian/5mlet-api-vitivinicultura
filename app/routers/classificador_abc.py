from fastapi import APIRouter, Depends, Query

from app.services.auth import verify_token
from app.services.classificador_abc import exportacao_abc

router = APIRouter(
    prefix="/abc_exportacao",
    tags=["Exportação ABC"],
    dependencies=[Depends(verify_token)]
)

@router.get(
    " ",
    summary="Este endpoint gera uma curva ABC dos dados de exportação de vinhos e derivados, já devidamente classificada, nos mostrando uma pespectiva dos maiores clientes desse tipo de produto.",
    description="Esta funcionalidade recebe o retorndo em formato json do endpoint de exportação, repassa o atributo dados desse retorno como parâmetro.",
    response_description="Retorna uma curva ABC de dados de exportação de vinhos e derivados."
    
)

def get_abc_exportacao(dados: str = Query(None)):
    return exportacao_abc(dados)