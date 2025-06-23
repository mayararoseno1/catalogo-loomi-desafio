from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import Tinta

db: Session = SessionLocal()

tintas_exemplo = [
    Tinta(
        nome="Branco Neve",
        cor="Branco",
        tipo_superficie="Parede Interna",
        ambiente="Sala",
        acabamento="Fosco",
        features="Antimofo, Lavável",
        linha="Suvinil Família Protegida"
    ),
    Tinta(
        nome="Azul Serenity",
        cor="Azul",
        tipo_superficie="Parede Externa",
        ambiente="Quarto",
        acabamento="Aveludado",
        features="Lavável",
        linha="Suvinil Criativa"
    )
]

db.add_all(tintas_exemplo)
db.commit()
db.close()

print("🌈 Dados inseridos com sucesso!")
