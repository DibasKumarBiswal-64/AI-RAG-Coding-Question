from pathlib import Path
from pypdf import PdfReader
from docx import Document

def load_document(file_path:str)->str:
    """
    Load and extract text from PDF, TXT, and DOCX files.
    """

    path=Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"file not found:{file_path}")
    
    extension=path.suffix.lower()

    
    #1. Load PDF
    if extension == ".pdf":
        reader=PdfReader(str(path))
        text=[]

        for page in reader.pages:
            page_text=page.extract_text()

            if page_text:
                text.append(page_text)

        return "\n".join(text)
    # 2. Load TXT
    elif extension == ".txt":
        return path.read_text(encoding="utf-8-sig")
    elif extension == ".docx":
        doc=Document(str(path))
        text=[]

        # Extract paragraphs
        for paragraph in doc.paragraphs:
            if paragraph.text.strip():
                text.append(paragraph.text)

        # Extract tables
        for table in doc.tables:
            for row in table.rows:
                    row_text=[
                        cell.text.strip() for cell in row.cells
                    ]
                    text.append(" | ".join(row_text))
        return "\n".join(text)

    else:
        raise ValueError(
             f"Unsupported file format: {extension}"
        )

