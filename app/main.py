from fastapi import FastAPI
from app.routers import assistente  # <- importa

app = FastAPI()

app.include_router(assistente.router)

@app.get("/")
def read_root():
    return {"message": "API IA de recomendação de tintas"}
