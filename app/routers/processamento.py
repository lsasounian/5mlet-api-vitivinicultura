from fastapi import APIRouter, Depends
from app.models.apiModel import ProcessamentoQueryParams
from app.services.auth import verify_token
from app.services.web_scraper import scrape_table

router = APIRouter(
    prefix="/processamento",
    tags=["Processamento"],
    dependencies=[Depends(verify_token)]
)

@router.get(
    "",
    summary="Obter dados de quantidade de uvas processadas no Rio Grande do Sul",
    description="Retorna os dados de quantidade de uvas processadas no Rio Grande do Sul"
)

def get_processamento(params: ProcessamentoQueryParams  = Depends()):
    return scrape_table("opt_03", params.ano, params.subopcao, params.categoria)