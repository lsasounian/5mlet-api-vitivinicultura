# 5mlet-api-vitivinicultura

**Vitivinicultura API – Embrapa** é uma API RESTful em Python que disponibiliza dados de vitivinicultura no Brasil extraídos do site http://vitibrasil.cnpuv.embrapa.br/. Fornece informações de produção, processamento, comercialização, importação, exportação.

---

## Funcionalidades

| Rota               | Método | Descrição                                                |
| ------------------ | ------ | -------------------------------------------------------- |
| `/login`           | POST   | Retorna um JWT para autenticar requisições subsequentes. |
| `/producao`        | GET    | Dados de produção de vinhos, sucos e derivados no RS.    |
| `/processamento`   | GET    | Quantidade de uvas processadas no RS.                    |
| `/comercializacao` | GET    | Dados de comercialização de vinhos e derivados no RS.    |
| `/importacao`      | GET    | Dados de importação de derivados de uva no Brasil.       |
| `/exportacao`      | GET    | Dados de exportação de derivados de uva no Brasil.       |
| `/abc_exportacao`  | GET    | Classificador ABC aplicado aos dados de exportação.      |

---

## Requisitos

* Python 3.7+

Dependências listadas em `requirements.txt`:

```
bs4
fastapi
requests
pydantic
PyJWT
uvicorn
pymongo
apscheduler
```

---

## Configuração do Ambiente

1. Clone o repositório:
```bash
git clone https://github.com/lsasounian/5mlet-api-vitivinicultura cd 5mlet-api-vitivinicultura

````

2. (Opcional) Crie e ative um ambiente virtual:
```bash
python -m venv .venv
source .venv/bin/activate   # Linux/macOS
.venv\Scripts\activate    # Windows
````

3. Instale as dependências:

```bash 
pip install -r requirements.txt
````

4. Variáveis de ambiente (locais ou via Vercel):
```bash
MONGODB_URI=<sua-connection-string-mongodb>
JWT_SECRET=<seu-segredo-para-JWT>
````

---

## Execução Local

Para rodar a API em desenvolvimento, execute:

```bash
uvicorn main:app --reload
```

Acesse o Swagger UI em:

```
http://localhost:8000/docs
```

---

## Deploy em Vercel

Esta API já está configurada para deploy automático no [Vercel](https://vercel.com):

1. Certifique-se de ter o arquivo `vercel.json` com as configurações de rota API.
2. No painel do Vercel, adicione as mesmas variáveis de ambiente definidas localmente.
3. Vincule o repositório Git e faça deploy.

Após deploy, a API estará disponível em:

```
https://<seu-projeto>.vercel.app/api
```

E a documentação interativa em:

```
https://<seu-projeto>.vercel.app/api/docs
```

---

## Colaborando

1. Faça um fork do repositório.
2. Crie uma branch de feature: `git checkout -b feature/nome-da-feature`.
3. Commit suas alterações: `git commit -am 'Descrição das alterações'`.
4. Envie sua branch: `git push origin feature/nome-da-feature`.
5. Abra um Pull Request.

---

## 📄 License

Distribuído sob a licença MIT. Veja [LICENSE](LICENSE) para mais detalhes.
