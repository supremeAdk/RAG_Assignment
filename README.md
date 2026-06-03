# Conversational RAG Backend with Interview Booking

## Overview

This project implements a Retrieval-Augmented Generation (RAG) backend using FastAPI.

The system supports:

* Document ingestion from PDF and TXT files
* Multiple text chunking strategies
* Embedding generation
* Vector storage using Qdrant
* Conversational RAG with Redis-based memory
* Interview booking using Llama 3 (Ollama)
* Metadata persistence using SQLite

---

## Architecture
FastAPI
│
├── Document Upload API
│   ├── PDF/TXT Extraction
│   ├── Chunking
│   ├── Embeddings
│   └── Qdrant Storage
│
└── Conversational RAG API
    ├── Retrieval
    ├── Redis Memory
    ├── Llama3 (Ollama)
    └── Interview Booking

## Tech Stack

* FastAPI
* SQLite
* SQLAlchemy
* Qdrant
* Redis
* Ollama
* Llama 3
* SentenceTransformers

---

## Features

### Document Ingestion

* Upload PDF files
* Upload TXT files
* Fixed-size chunking
* Recursive chunking
* Embedding generation
* Vector storage in Qdrant
* Metadata persistence

### Conversational RAG

* Custom retrieval pipeline
* No RetrievalQAChain
* Context retrieval from Qdrant
* Multi-turn conversations
* Redis-based chat memory

### Interview Booking

Users can schedule interviews using natural language.

Example:

Book an interview for John Doe on June 10 at 3 PM. Email [john@example.com](mailto:john@example.com)

The system extracts:

* Name
* Email
* Date
* Time

and stores the booking in SQLite.

---

## API Endpoints

### Upload Document

POST /documents/upload

Form Data:

* file
* chunk_strategy

Chunk Strategy Values:

* fixed
* recursive

---

### Chat

POST /chat

Request:

{
"session_id": "user123",
"question": "What is the leave policy?"
}

---

## Setup Instructions

### Clone Repository

git clone <repository-url>

cd assignment-palmmind

### Create Virtual Environment

python -m venv venv

venv\Scripts\activate

### Install Dependencies

pip install -r requirements.txt

### Start Qdrant

docker run -p 6333:6333 qdrant/qdrant

### Start Redis

docker run -p 6379:6379 redis

### Start Ollama

ollama run llama3

### Run FastAPI

uvicorn main:app --reload

---

## Design Decisions

* Qdrant selected for vector storage
* Redis used for conversation memory
* SQLite used for lightweight persistence
* Custom retrieval pipeline implemented instead of RetrievalQAChain
* Modular architecture for maintainability and scalability
