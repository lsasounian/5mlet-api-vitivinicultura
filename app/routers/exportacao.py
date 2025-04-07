from fastapi import APIRouter, Depends
from app.models.apiModel import ExportacaoQueryParams
from app.services.auth import verify_token
from app.services.web_scraper import scrape_table

router = APIRouter(
    prefix="/exportacao",
    tags=["Exportação"],
    dependencies=[Depends(verify_token)]
)

@router.get(
    "",
    summary="Obter dados de exportação de derivados de uva",
    description="Retorna os dados de exportação de derivados de uva"
)

def get_exportacao(params: ExportacaoQueryParams= Depends()):
    return scrape_table("opt_06", params.ano, params.subopcao)