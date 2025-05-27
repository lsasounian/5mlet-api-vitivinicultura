from fastapi import Depends, Query
from pydantic import BaseModel
from typing import Optional

class ProducaoQueryParams:
    def __init__(
        self,
        ano: Optional[int] = Query(
            None,
            title="Ano",
            description="Ano de referência da produção.",
            ge=1970,
            le=2023,
            example=2023
        )
    ):
        self.ano = ano

class ProcessamentoQueryParams:
    def __init__(
        self,
        ano: Optional[int] = Query(
            None,
            title="Ano",
            description="Ano de referência da produção.",
            ge=1970,
            le=2023,
            example=2023
        ),
        subopcao: Optional[str] = Query(
            None,
            title="Sub Opção",
            description="Subopção do processamento. Caso não saiba o valor, faça uma requisição sem este parametro para ver as opções disponíveis.",
            example="subopt_01"
        )
    ):
        self.ano = ano
        self.subopcao = subopcao

class ComercializacaoQueryParams:
    def __init__(
        self,
        ano: Optional[int] = Query(
            None,
            title="Ano",
            description="Ano de referência da produção.",
            ge=1970,
            le=2023,
            example=2023
        )
    ):
        self.ano = ano

class ImportacaoQueryParams:
    def __init__(
        self,
        ano: Optional[int] = Query(
            None,
            title="Ano",
            description="Ano de referência da produção.",
            ge=1970,
            le=2023,
            example=2023
        ),
        subopcao: Optional[str] = Query(
            None,
            title="Sub Opção",
            description="Subopção do processamento. Caso não saiba o valor, faça uma requisição sem este parametro para ver as opções disponíveis.",
            example="subopt_01"
        )
    ):
        self.ano = ano
        self.subopcao = subopcao

class ExportacaoQueryParams:
    def __init__(
        self,
        ano: Optional[int] = Query(
            None,
            title="Ano",
            description="Ano de referência da produção.",
            ge=1970,
            le=2023,
            example=2023
        ),
        subopcao: Optional[str] = Query(
            None,
            title="Sub Opção",
            description="Subopção do processamento. Caso não saiba o valor, faça uma requisição sem este parametro para ver as opções disponíveis.",
            example="subopt_01"
        )
    ):
        self.ano = ano
        self.subopcao = subopcao