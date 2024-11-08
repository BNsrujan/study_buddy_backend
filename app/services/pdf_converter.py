import pdfplumber

def convert_pdf_to_text(file_content):
    with pdfplumber.open(file_content) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text
