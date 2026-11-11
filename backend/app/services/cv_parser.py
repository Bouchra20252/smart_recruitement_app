import fitz


def extract_text_from_pdf(file_content: bytes) -> str:

    document = fitz.open(
        stream=file_content,
        filetype="pdf"
    )

    extracted_text = ""

    for page in document:
        extracted_text += page.get_text()

    document.close()

    return extracted_text