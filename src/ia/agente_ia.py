from app.database import SessionLocal
from app.models import Tinta
from app.ia.image_generator import gerar_imagem_dalle
from langchain.chains import LLMChain
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
import os

llm = ChatOpenAI(openai_api_key=os.getenv("OPENAI_API_KEY"))

prompt_template = PromptTemplate.from_template("""
Você é um assistente de decoração. Receba a descrição do cliente e recomende uma tinta da base disponível.
Diga o nome da tinta, acabamento e cor. Não invente tintas que não existem na base.

Base de tintas disponíveis:
{tintas}

Descrição do cliente:
{descricao}

Responda no formato:
Recomendo a TINTA_NOME com acabamento TINTA_ACABAMENTO. Veja abaixo uma simulação da aplicação da cor TINTA_COR.
""")




def responder_com_imagem(descricao: str):
    db = SessionLocal()
    tintas = db.query(Tinta).all()
    base_tintas = "\n".join([f"{t.nome}, {t.cor}, {t.acabamento}" for t in tintas])

    chain = LLMChain(llm=llm, prompt=prompt_template)
    resposta = chain.run(tintas=base_tintas, descricao=descricao)

    
    tinta_selecionada = next((t for t in tintas if t.nome in resposta), None)

    if not tinta_selecionada:
        return {"resposta": "Desculpe, não encontrei uma tinta adequada."}

    prompt_img = f"varanda pintada com a cor {tinta_selecionada.cor} em estilo moderno"
    url_imagem = gerar_imagem_dalle(prompt_img)

    return {
        "resposta": resposta,
        "imagem": url_imagem
    }
