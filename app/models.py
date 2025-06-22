from sqlalchemy import Column, Integer, String
from app.database import Base

class Tinta(Base):
    _tablename_ = "tintas"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    cor = Column(String, nullable=False)
    tipo_superficie = Column(String)
    ambiente = Column(String)
    acabamento = Column(String)
    features = Column(String)
    linha = Column(String)