from app.database import SessionLocal
from app.models import Tinta

db = SessionLocal()

# Lista de tintas 
tintas = [
    Tinta(
        nome="Suvinil Toque de Seda",
        cor="Branco Neve",
        tipo_superficie="Alvenaria",
        ambiente="Interior",
        acabamento="Aveludado",
        features="Lavável, sem cheiro",
        linha="Premium"
    ),
    Tinta(
        nome="Suvinil Fosco Completo",
        cor="Cinza Urbano",
        tipo_superficie="Parede",
        ambiente="Interior",
        acabamento="Fosco",
        features="Alta cobertura, sem cheiro",
        linha="Standard"
    ),
    Tinta(
        nome="Suvinil Clássica",
        cor="Bege Areia",
        tipo_superficie="Parede",
        ambiente="Interior e Exterior",
        acabamento="Fosco",
        features="Boa cobertura, lavável",
        linha="Econômica"
    )
]


for tinta in tintas:
    db.add(tinta)

db.commit()
db.close()

print("✔️ Base de tintas populada com sucesso.")