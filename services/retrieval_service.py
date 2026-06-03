from db.qdrant_db import client

from services.embedding_service import (
    generate_embedding
)

from services.qdrant_service import (
    COLLECTION_NAME
)


def retrieve_context(
    question: str,
    limit: int = 3
):
    vector = generate_embedding(question)

    results = client.query_points(
        collection_name=COLLECTION_NAME,
        query=vector,
        limit=limit
    )

    return [
        point.payload["text"]
        for point in results.points
    ]