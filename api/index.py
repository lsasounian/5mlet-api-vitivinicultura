import sys, os

# garante que o main.py (em raiz) seja encontrado
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from main import app   # <-- fastapi.FastAPI()