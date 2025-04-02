# Usa imagem oficial do Python
FROM python:3.11-slim

# Define diretório de trabalho
WORKDIR /app

# Copia os arquivos da aplicação
COPY . .

# Instala as dependências
RUN pip install --no-cache-dir fastapi uvicorn requests beautifulsoup4 python-jose[cryptography]

# Expõe a porta padrão do Uvicorn
EXPOSE 8000

# Comando de inicialização da API
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
