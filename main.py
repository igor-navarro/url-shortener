import random
import string

from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from pydantic import BaseModel, HttpUrl

app = FastAPI(title="Encurtador de URL")

urls = {}  # guarda: codigo -> url original


class UrlEntrada(BaseModel):
    url: HttpUrl


def gerar_codigo(tamanho=6):
    caracteres = string.ascii_letters + string.digits
    return "".join(random.choices(caracteres, k=tamanho))


@app.get("/")
def inicio():
    return {"mensagem": "Encurtador no ar!"}


@app.post("/encurtar")
def encurtar(dados: UrlEntrada):
    codigo = gerar_codigo()
    while codigo in urls:
        codigo = gerar_codigo()
    urls[codigo] = str(dados.url)
    return {"codigo": codigo, "url_curta": f"http://localhost:8000/{codigo}"}


@app.get("/{codigo}")
def redirecionar(codigo: str):
    url = urls.get(codigo)
    if url is None:
        raise HTTPException(status_code=404, detail="Código não encontrado")
    return RedirectResponse(url)