from fastapi import FastAPI

from db.sqlite_db import Base, engine

import models.document
import models.booking

from api.document import router as document_router
from api.chat import router as chat_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="RAG Assignment"
)

app.include_router(document_router)
app.include_router(chat_router)