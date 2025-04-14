import logging
from pymongo import MongoClient

# Configuração do logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Configuração do MongoDB
MONGO_URI = "mongodb://localhost:27017"
DATABASE_NAME = "vitivinicultura"


class ExportacaoRepository:

    COLLECTION_NAME_EXPORTACAO_ABC = "abc_exportacao"
    
    def __init__(self):
        self.client = MongoClient(MONGO_URI)
        self.db = self.client[DATABASE_NAME]
        self.collection = self.db[COLLECTION_NAME_EXPORTACAO_ABC]

    def persistir_exportacao(self, dados: str):
        try:
            logger.info("Iniciando a persistência dos Dados.")
            self.collection.insert_one(dados)  # Insere os dados
            logger.info("Dados persistidos com sucesso.")
        except Exception as e:
            logger.error(f"Erro ao persistir dados : {e}")
