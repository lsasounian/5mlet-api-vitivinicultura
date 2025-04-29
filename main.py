from fastapi import FastAPI
from app.routers import login, producao, processamento, comercializacao, importacao, exportacao, classificador_abc
from mangum import Mangum

app = FastAPI(title="Vitivinicultura API - Embrapa")

@app.get("/")
async def root():
    return {"greeting": "Olá, bem vindo a API de Vitivinicultura da Embrapa", "message": "Dúvidas? Faça uma requisição /docs e veja a documentação completa"}

app.include_router(login.router)
app.include_router(producao.router)
app.include_router(processamento.router)
app.include_router(comercializacao.router)
app.include_router(importacao.router)
app.include_router(exportacao.router)
app.include_router(classificador_abc.router)

handler = Mangum(app)