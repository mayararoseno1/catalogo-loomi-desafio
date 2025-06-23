from fastapi import APIRouter
from pydantic import BaseModel
from app.ia.agente_ia import responder_com_imagem

router = APIRouter()

class Pergunta(BaseModel):
    descricao: str

@router.post("/assistente/")
def assistente_resposta(pergunta: Pergunta):
    return responder_com_imagem(pergunta.descricao)
