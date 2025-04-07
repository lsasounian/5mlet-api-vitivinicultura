from fastapi import APIRouter, Depends
from app.models.apiModel import ImportacaoQueryParams
from app.services.auth import verify_token
from app.services.web_scraper import scrape_table

router = APIRouter(
    prefix="/importacao",
    tags=["Importação"],
    dependencies=[Depends(verify_token)]
)

@router.get(
    "",
    summary="Obter dados de importação de derivados de uva",
    description="Retorna os dados de importação de derivados de uva"
)

def get_importacao(params: ImportacaoQueryParams = Depends()):
    return scrape_table("opt_05", params.ano, params.subopcao)