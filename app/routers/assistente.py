from fastapi import APIRouter
from pydantic import BaseModel
from app.ia.agente_ia import responder

router = APIRouter(prefix="/assistente", tags=["assistente"])

class Pergunta(BaseModel):
    mensagem: str

@router.post("/")
def responder_pergunta(pergunta: Pergunta):
    resposta = responder(pergunta.mensagem)
    return {"resposta": resposta}
