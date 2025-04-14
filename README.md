# 5mlet-api-vitivinicultura

É uma biblioteca Python com objetivo de análise de dados de viticultura no Brasil. Ela permite obter dados do site http://vitibrasil.cnpuv.embrapa.br/, obtendo dados de produção, processamento, comercialização, importação e exportação.

## Funcionalidades

- Obter dados históricos de ações usando a API do Alpha Vantage.
- Calcular retorno diário das ações.
- Visualizar gráficos de preços de fechamento das ações.

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

Para executar, execute

`python -m venv .venv`

`.venv\Scripts\activate`

## Uso

Depois de instalar todas dependências com o comando `pip install -r requirements.txt`, você pode executar o comando a seguir:

`uvicorn app.main:app --reload`

Acesse:

http://localhost:8000/docs

## Contribuindo

1. Faça um fork do repositório
2. Crie uma nova branch (`git checkout -b feature/include-cache`)
3. Commit suas mudanças (`git commit -am 'Add some feature'`)
4. Push para a branch (`git push origin feature/include-cache`)
5. Abra um Pull Request

## Licença

Distribuído sob a licença MIT. Veja `LICENSE` para mais informações.
