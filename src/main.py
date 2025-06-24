from fastapi import FastAPI
from app.routers import assistente, tintas

app = FastAPI()

app.include_router(assistente.router)
app.include_router(tintas.router)

@app.get("/")
def read_root():
    return {"message": "API IA de recomendação de tintas"}
