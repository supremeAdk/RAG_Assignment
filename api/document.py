import os
import uuid

from fastapi import (
    APIRouter,
    UploadFile,
    File,
    Form,
    HTTPException
)

from sqlalchemy.orm import Session

from db.sqlite_db import SessionLocal

from models.document import Document

from services.document_service import (
    extract_pdf_text,
    extract_txt_text
)

from services.chunk_service import (
    fixed_chunk,
    recursive_chunk
)

from services.embedding_service import (
    generate_embedding
)

from services.qdrant_service import (
    create_collection,
    COLLECTION_NAME
)

from db.qdrant_db import client

from qdrant_client.models import PointStruct


router = APIRouter()


@router.post("/documents/upload")
async def upload_document(
    file: UploadFile = File(...),
    chunk_strategy: str = Form(...)
):

    create_collection()

    extension = file.filename.split(".")[-1]

    if extension not in ["pdf", "txt"]:
        raise HTTPException(
            status_code=400,
            detail="Only PDF and TXT files allowed"
        )

    os.makedirs("uploads", exist_ok=True)

    file_path = f"uploads/{file.filename}"

    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    if extension == "pdf":
        text = extract_pdf_text(file_path)
    else:
        text = extract_txt_text(file_path)

    if chunk_strategy == "fixed":
        chunks = fixed_chunk(text)

    elif chunk_strategy == "recursive":
        chunks = recursive_chunk(text)

    else:
        raise HTTPException(
            status_code=400,
            detail="Invalid chunk strategy"
        )

    points = []

    for idx, chunk in enumerate(chunks):

        vector = generate_embedding(chunk)

        points.append(
            PointStruct(
                id=str(uuid.uuid4()),
                vector=vector,
                payload={
                    "text": chunk,
                    "filename": file.filename
                }
            )
        )

    client.upsert(
        collection_name=COLLECTION_NAME,
        points=points
    )

    db: Session = SessionLocal()

    document = Document(
        filename=file.filename,
        chunk_strategy=chunk_strategy
    )

    db.add(document)
    db.commit()

    db.close()

    return {
        "status": "success",
        "chunks": len(chunks)
    }