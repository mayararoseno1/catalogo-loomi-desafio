# 🎨 Catálogo Loomi - Desafio Técnico

Este repositório foi desenvolvido como parte do **desafio técnico da Loomi**. O objetivo é criar uma API que receba uma descrição em linguagem natural do usuário e, com base em uma base de dados de tintas, recomende uma cor adequada e gere uma imagem simulando a aplicação da cor.

---

## 🚀 Tecnologias Utilizadas

* **Python 3.10**
* **FastAPI**
* **PostgreSQL**
* **SQLAlchemy**
* **Docker & Docker Compose**
* **OpenAI API (DALL·E e GPT via LangChain)**
* **LangChain**
* **Uvicorn**

---

## 🧠 Funcionalidade

A aplicação permite que o usuário envie uma descrição como:

```json
{
  "descricao": "Quero pintar minha varanda de azul claro, algo moderno e resistente ao tempo"
}
```

A IA analisa o texto, recomenda uma tinta cadastrada e retorna uma imagem gerada com a cor sugerida. Exemplo de resposta:

```json
{
  "resposta": "Recomendo a Suvinil Azul Sereno com acabamento fosco. Veja abaixo uma simulação da aplicação da cor azul claro.",
  "imagem": "https://url-gerada-da-imagem.com"
}
```

---

## 🛠️ Como rodar o projeto

### ✅ Pré-requisitos

* Docker e Docker Compose instalados
* Chave da API da OpenAI ([https://platform.openai.com/account/api-keys](https://platform.openai.com/account/api-keys))

### 📁 Clonar o projeto

```bash
git clone https://github.com/seu-user/catalogo-loomi-desafio.git
cd catalogo-loomi-desafio
```

### 🥪 Variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto com o seguinte conteúdo:

```
OPENAI_API_KEY=sua-chave-da-openai
```

### 🐳 Subir o ambiente com Docker

```bash
docker-compose up --build
```

O FastAPI estará disponível em:
👉 [http://localhost:8000](http://localhost:8000)

A documentação interativa da API pode ser acessada em:
👉 [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🥪 Como testar a IA

### Rota: `POST /assistente/`

Exemplo de requisição no Postman ou cURL:

```json
{
  "descricao": "Gostaria de pintar a sala com uma cor aconchegante e sofisticada"
}
```

Exemplo de resposta:

```json
{
  "resposta": "Recomendo a Coral Bege Fino com acabamento acetinado. Veja abaixo uma simulação da aplicação da cor bege claro.",
  "imagem": "https://url-da-imagem-gerada.com"
}
```

---

## 🗂️ Estrutura do Projeto

```
app/
├── main.py                  # Entrada principal da API
├── database.py              # Conexão e engine do banco de dados
├── models.py                # Modelos SQLAlchemy
├── routers/
│   ├── tintas.py            # Rota para listar tintas (GET /tintas/)
│   └── assistente.py        # Rota principal de recomendação e imagem
├── ia/
    ├── agente_ia.py         # Lógica de recomendação de tinta + geração de prompt
    └── image_generator.py   # Função para gerar imagem com DALL·E
```

---

## 📝 Observações

* Apenas tintas cadastradas são utilizadas nas respostas da IA.
* A imagem é gerada com base na cor sugerida, usando a API da OpenAI (modelo DALL·E).
* O projeto está isolado em containers, facilitando a execução em qualquer ambiente.
* Os testes automatizados foram removidos após ajustes no foco da funcionalidade principal.

---

## 👩‍💻 Desenvolvido por

Mayara Roseno
Desafio Técnico - Loomi · 2025
