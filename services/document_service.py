from pypdf import PdfReader


def extract_pdf_text(path: str) -> str:

    reader = PdfReader(path)

    text = ""

    for page in reader.pages:
        text += page.extract_text() or ""

    return text


def extract_txt_text(path: str) -> str:

    with open(
        path,
        "r",
        encoding="utf-8"
    ) as f:

        return f.read()