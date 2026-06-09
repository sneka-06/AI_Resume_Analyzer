import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            "..",
            "src"
        )
    )
)

from pdf_extractor import extract_text


pdfs = [
    "resumes/resume1.pdf",
    "resumes/resume2.pdf",
    "resumes/resume3.pdf",
    "resumes/fake.pdf",
]

for pdf in pdfs:

    result = extract_text(pdf)

    print("=" * 50)
    print(pdf)
    print("=" * 50)

    if result["success"]:
        print(result["text"][:500])
    else:
        print(result["message"])

    print("\n")