from fastapi import APIRouter
from pydantic import BaseModel
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

router = APIRouter()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class ImagemRequest(BaseModel):
    descricao: str

@router.post("/gerar-imagem")
def gerar_imagem(request: ImagemRequest):
    try:
        response = client.images.generate(
            model="dall-e-3",
            prompt=request.descricao,
            size="1024x1024",
            quality="standard",
            n=1
        )
        url_imagem = response.data[0].url
        return {"url_imagem": url_imagem}
    except Exception as e:
        return {"erro": str(e)}
