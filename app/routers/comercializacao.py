from fastapi import APIRouter, Depends
from app.models.apiModel import ComercializacaoQueryParams
from app.services.auth import verify_token
from app.services.web_scraper import scrape_table

router = APIRouter(
    prefix="/comercializacao",
    tags=["Comercialização"],
    dependencies=[Depends(verify_token)]
)

@router.get(
    "",
    summary="Obter dados de comercialização de vinhos e derivados no Rio Grande do Sul",
    description="Retorna os dados de comercialização de vinhos e derivados no Rio Grande do Sul"
)

def get_comercializacao(params: ComercializacaoQueryParams  = Depends()):
    return scrape_table("opt_04", params.ano)