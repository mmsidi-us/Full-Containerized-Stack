# Full-Containerized RAG Stack

A containerized Retrieval-Augmented Generation (RAG) system built with FastAPI, Streamlit, ChromaDB, and Ollama.

## Architecture

* **Frontend:** Streamlit interactive UI
* **Backend:** FastAPI REST API
* **Vector DB:** ChromaDB
* **LLM Engine:** Ollama running Llama 3.2 (1B)

## Quick Start

1. Clone the repository:
   ```bash
   git clone [https://github.com/mmsidi-us/Full-Containerized-Stack.git](https://github.com/mmsidi-us/Full-Containerized-Stack.git)
   cd Full-Containerized-Stack

2. Start the services:
   docker compose up -d

3. Download the Ollama model:
   docker compose exec ollama ollama pull llama3.2:1b
   
4. Access the applications:
   Streamlit UI: http://localhost:8501
   FastAPI Docs: http://localhost:8000/docs

