# URL Shortener

API REST para encurtar URLs, feita com **FastAPI** e **PostgreSQL**.

Você envia uma URL longa, recebe um código curto e, ao acessar o link curto, é redirecionado para o endereço original. Cada acesso é contado.

## Tecnologias
- Python 3
- FastAPI + Uvicorn
- PostgreSQL (rodando em Docker)
- SQLAlchemy

## Endpoints

| Método | Rota | O que faz |
|--------|------|-----------|
| GET | `/` | Verifica se a API está no ar |
| POST | `/encurtar` | Recebe uma URL e devolve um código curto |
| GET | `/{codigo}` | Redireciona para a URL original e conta o clique |

## Como rodar

1. Clone o repositório:
   ```
   git clone https://github.com/igor-navarro/url-shortener.git
   cd url-shortener
   ```
2. Suba o banco de dados:
   ```
   docker compose up -d
   ```
3. Crie e ative o ambiente virtual (Windows):
   ```
   python -m venv venv
   venv\Scripts\activate
   ```
4. Instale as dependências:
   ```
   pip install -r requirements.txt
   ```
5. Inicie a API:
   ```
   uvicorn main:app --reload
   ```
6. Abra a documentação interativa em http://localhost:8000/docs

## Próximos passos
- [ ] Testes automatizados
- [ ] Deploy na nuvem
