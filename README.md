# URL Shortener

API REST para encurtar URLs, feita com **FastAPI** (Python).

Você envia uma URL longa, recebe um código curto e, ao acessar o link curto, é redirecionado para o endereço original.

## Tecnologias
- Python 3
- FastAPI
- Uvicorn
- Pydantic (validação da URL)

## Endpoints

| Método | Rota | O que faz |
|--------|------|-----------|
| GET | `/` | Verifica se a API está no ar |
| POST | `/encurtar` | Recebe uma URL e devolve um código curto |
| GET | `/{codigo}` | Redireciona para a URL original |

### Exemplo

Requisição:
```json
POST /encurtar
{"url": "https://www.github.com"}
```

Resposta:
```json
{
  "codigo": "Tuy8Ln",
  "url_curta": "http://localhost:8000/Tuy8Ln"
}
```

## Como rodar

1. Clone o repositório:
   ```
   git clone https://github.com/igor-navarro/url-shortener.git
   cd url-shortener
   ```
2. Crie e ative o ambiente virtual (Windows):
   ```
   python -m venv venv
   venv\Scripts\activate
   ```
3. Instale as dependências:
   ```
   pip install -r requirements.txt
   ```
4. Inicie a API:
   ```
   uvicorn main:app --reload
   ```
5. Abra a documentação interativa em http://localhost:8000/docs

## Status do projeto

Os links são guardados **em memória**, então somem quando o servidor reinicia.

## Próximos passos
- [ ] Salvar os links no PostgreSQL (rodando com Docker)
- [ ] Contador de cliques por link
- [ ] Testes automatizados
