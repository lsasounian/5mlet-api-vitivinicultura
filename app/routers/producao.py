from fastapi import APIRouter, Depends
from app.models.apiModel import ProducaoQueryParams
from app.services.auth import verify_token
from app.services.web_scraper import scrape_table

router = APIRouter(
    prefix="/producao",
    tags=["Produção"],
    dependencies=[Depends(verify_token)]
)

@router.get(
    "",
    summary="Obter dados de produção de vinhos, sucos e derivados do Rio Grande do Sul",
    description="Retorna os dados de produção de vinhos, sucos e derivados do Rio Grande do Sul"
)
def get_producao(params: ProducaoQueryParams = Depends()):
    return scrape_table("opt_02", params.ano)
