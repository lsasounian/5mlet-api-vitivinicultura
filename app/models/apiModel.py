from fastapi import Depends, Query
from pydantic import BaseModel
from typing import Optional

class ProducaoQueryParams:
    def __init__(
        self,
        ano: Optional[int] = Query(
            None,
            title="Ano",
            description="Ano de referência da produção. Exemplo: 2023.",
            ge=1970,
            le=2023,
            example=2023
        ),
        categoria: Optional[str] = Query(
            None,
            title="Categoria",
            description="Categoria da produção. Exemplo: 'vinho', 'suco', 'uva'.",
            example="vinho"
        ),
    ):
        self.ano = ano
        self.categoria = categoria

class ProcessamentoQueryParams:
    def __init__(
        self,
        ano: Optional[int] = Query(
            None,
            title="Ano",
            description="Ano de referência da produção. Exemplo: 2023.",
            ge=1970,
            le=2023,
            example=2023
        ),
        categoria: Optional[str] = Query(
            None,
            title="Categoria",
            description="Categoria da produção. Exemplo: 'vinho', 'suco', 'uva'.",
            example="vinho"
        ),
        subopcao: Optional[str] = Query(
            None,
            title="Sub Opção",
            description="Categoria da produção. Exemplo: 'vinho', 'suco', 'uva'.",
            example="vinho"
        )
    ):
        self.ano = ano
        self.categoria = categoria
        self.subopcao = subopcao

class ComercializacaoQueryParams:
    def __init__(
        self,
        ano: Optional[int] = Query(
            None,
            title="Ano",
            description="Ano de referência da produção. Exemplo: 2023.",
            ge=1970,
            le=2023,
            example=2023
        ),
        categoria: Optional[str] = Query(
            None,
            title="Categoria",
            description="Categoria da produção. Exemplo: 'vinho', 'suco', 'uva'.",
            example="vinho"
        ),
    ):
        self.ano = ano
        self.categoria = categoria

class ImportacaoQueryParams:
    def __init__(
        self,
        ano: Optional[int] = Query(
            None,
            title="Ano",
            description="Ano de referência da produção. Exemplo: 2023.",
            ge=1970,
            le=2023,
            example=2023
        ),
        subopcao: Optional[str] = Query(
            None,
            title="Sub Opção",
            description="Categoria da produção. Exemplo: 'vinho', 'suco', 'uva'.",
            example="vinho"
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
            description="Ano de referência da produção. Exemplo: 2023.",
            ge=1970,
            le=2023,
            example=2023
        ),
        subopcao: Optional[str] = Query(
            None,
            title="Sub Opção",
            description="Categoria da produção. Exemplo: 'vinho', 'suco', 'uva'.",
            example="vinho"
        )
    ):
        self.ano = ano
        self.subopcao = subopcao