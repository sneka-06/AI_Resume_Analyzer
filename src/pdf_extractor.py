from pypdf import PdfReader


def extract_text(pdf_path):
    """
    Extract text from a PDF file.
    """

    try:
        reader = PdfReader(pdf_path)

        extracted_text = []

        for page in reader.pages:
            page_text = page.extract_text()

            if page_text:
                extracted_text.append(page_text)

        full_text = "\n".join(extracted_text)

        if not full_text.strip():
            return {
                "success": False,
                "message": "PDF appears to be scanned or image-only.",
                "text": None
            }

        return {
            "success": True,
            "message": "Text extracted successfully.",
            "text": full_text
        }

    except FileNotFoundError:
        return {
            "success": False,
            "message": f"File not found: {pdf_path}",
            "text": None
        }

    except Exception as e:
        return {
            "success": False,
            "message": str(e),
            "text": None
        }