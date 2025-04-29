from mangum import Mangum
import sys
import os

# Adicione o diretório raiz ao caminho do Python
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Importe a aplicação FastAPI do arquivo main.py
from main import app

# Crie o handler para o Vercel
handler = Mangum(app)