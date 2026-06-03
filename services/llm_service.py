import ollama


def generate_response(
    context: str,
    history: str,
    question: str
) -> str:

    prompt = f"""
You are a helpful assistant.

Conversation History:
{history}

Context:
{context}

Question:
{question}

Answer using the provided context whenever possible.
"""

    response = ollama.chat(
        model="llama3",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]