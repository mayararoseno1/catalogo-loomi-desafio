import os
import pandas as pd
from dotenv import load_dotenv
from langchain.text_splitter import CharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import DataFrameLoader


load_dotenv()
openai_key = os.getenv("OPENAI_API_KEY")


csv_path = "app/data/Base_de_Dados_de_Tintas_Suvinil.csv"


df = pd.read_csv(csv_path)


df["text"] = df.apply(lambda row: " | ".join([str(v) for v in row.values]), axis=1)


loader = DataFrameLoader(df[["text"]], page_content_column="text")
documents = loader.load()


splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = splitter.split_documents(documents)


embeddings = OpenAIEmbeddings(openai_api_key=openai_key)

db = FAISS.from_documents(chunks, embeddings)

db.save_local("app/ia/faiss_tintas")

print("✅ Embeddings gerados e FAISS salvo com sucesso!")
