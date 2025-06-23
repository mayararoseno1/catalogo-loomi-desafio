import os
from dotenv import load_dotenv
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings, ChatOpenAI 
from langchain.chains import RetrievalQA

load_dotenv() 

openai_key = os.getenv("OPENAI_API_KEY")

FAISS_INDEX_PATH = "ia/faiss_tintas"


vectorstore = FAISS.load_local(
    "ia/faiss_tintas", 
    OpenAIEmbeddings(openai_api_key=openai_key),
    allow_dangerous_deserialization=True
)

llm = ChatOpenAI(openai_api_key=openai_key, temperature=0.5)

qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=vectorstore.as_retriever(search_kwargs={"k": 3}),
    chain_type="stuff"
)

def responder(pergunta: str):
    try:
        resposta = qa_chain.run(pergunta)
        return resposta
    except Exception as e:
        return f"Erro ao gerar resposta: {str(e)}"

if __name__ == "__main__":
    while True:
        pergunta = input("\nUsuário: ")
        if pergunta.lower() in ["sair", "exit", "quit"]:
            break
        resposta = responder(pergunta)
        print("\nIA:", resposta)