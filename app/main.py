from fastapi import FastAPI, Depends, HTTPException, status, Query
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel
import requests
from app.services.web_scraper import scrape_table
from app.models.model import UserLogin
from app.services.auth import create_token, verify_token
import jwt
import os
from datetime import datetime, timedelta

app = FastAPI(title="Vitivinicultura API - Embrapa")

@app.post("/login")
def login(user: UserLogin):
    if user.username == "admin" and user.password == "123456":
        token = create_token(user.username)
        return {"access_token": token}
    raise HTTPException(status_code=401, detail="Credenciais inválidas")

@app.get("/producao", dependencies=[Depends(verify_token)])
def get_producao(ano: int = Query(None), categoria: str = Query(None)):
    return scrape_table("opt_02", ano, categoria)

@app.get("/processamento", dependencies=[Depends(verify_token)])
def get_processamento(ano: int = Query(None), subopcao: str = Query(None), categoria: str = Query(None)):
    return scrape_table("opt_03", ano, subopcao, categoria)

@app.get("/comercializacao", dependencies=[Depends(verify_token)])
def get_comercializacao(ano: int = Query(None), categoria: str = Query(None)):
    return scrape_table("opt_04", ano, categoria)

@app.get("/importacao", dependencies=[Depends(verify_token)])
def get_importacao(ano: int = Query(None), subopcao: str = Query(None), categoria: str = Query(None)):
    return scrape_table("opt_05", ano, subopcao, categoria)

@app.get("/exportacao", dependencies=[Depends(verify_token)])
def get_exportacao(ano: int = Query(None), subopcao: str = Query(None), categoria: str = Query(None)):
    return scrape_table("opt_06", ano, subopcao, categoria)

