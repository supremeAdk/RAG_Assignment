from typing import List


def fixed_chunk(
    text: str,
    size: int = 500
) -> List[str]:

    return [
        text[i:i + size]
        for i in range(0, len(text), size)
    ]


def recursive_chunk(
    text: str,
    size: int = 500
) -> List[str]:

    paragraphs = text.split("\n")

    chunks = []
    current = ""

    for paragraph in paragraphs:

        if len(current) + len(paragraph) < size:
            current += paragraph + "\n"

        else:
            chunks.append(current)
            current = paragraph

    if current:
        chunks.append(current)

    return chunks