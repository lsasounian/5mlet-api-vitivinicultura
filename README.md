# 5mlet-api-vitivinicultura

Vitivinicultura API - Embrapa é uma biblioteca Python com objetivo de análise de dados de viticultura no Brasil. Ela permite obter dados do site http://vitibrasil.cnpuv.embrapa.br/, obtendo dados de produção, processamento, comercialização, importação e exportação.

## Funcionalidades

- /login - Retorna o JWT Token para utilizar nos requests da API.
- /producao - Retorna os dados de produção de vinhos, sucos e derivados do Rio Grande do Sul.
- /processamento - Retorna os dados de quantidade de uvas processadas no Rio Grande do Sul.
- /comercializacao - Retorna os dados de comercialização de vinhos e derivados no Rio Grande do Sul.
- /importacao - Retorna os dados de importação de derivados de uva.
- /exportacao - Retorna os dados de exportação de derivados de uva.
- /abc_exportacao - Retorna os dados de Classificador ABC.

## Requisitos

- Python 3.6+
- bs4
- fastapi
- requests
- jwt
- pydantic
- PyJWT
- uvicorn
- pymongo
- apscheduler
- datetime
- logging

## Configuração

Para executar, execute no diretório raiz do projeto:

`python -m venv .venv`

`.venv\Scripts\activate`

## Uso

Depois de instalar todas dependências com o comando `pip install -r requirements.txt`, após essa fase você já pode executar o comando a seguir:

`uvicorn app.main:app --reload`

e acesse o endereço:

http://localhost:8000/docs

## Contribuindo

1. Faça um fork do repositório
2. Crie uma nova branch (`git checkout -b feature/include-cache`)
3. Commit suas mudanças (`git commit -am 'Add some feature'`)
4. Push para a branch (`git push origin feature/include-cache`)
5. Abra um Pull Request

## Licença

Distribuído sob a licença MIT. Veja `LICENSE` para mais informações.
