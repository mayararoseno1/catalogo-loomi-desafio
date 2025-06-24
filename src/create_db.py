
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from app.database import engine, Base
from app import models

print("Criando as tabelas no banco de dados...")
Base.metadata.create_all(bind=engine)
print("Feito!")