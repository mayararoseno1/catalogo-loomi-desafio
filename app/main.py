from fastapi import FastAPI
from app.routers import tinta, assistente

app = FastAPI()

app.include_router(tinta.router)
app.include_router(assistente.router)

@app.get("/")
def read_root():
    return {"message": "API do Catálogo de Tintas com IA"}