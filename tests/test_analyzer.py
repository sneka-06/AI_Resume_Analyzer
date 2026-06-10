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
from analyzer import analyze_resume


pdf_path = "resumes/resume1.pdf"

result = extract_text(pdf_path)

if result["success"]:

    analysis = analyze_resume(
        result["text"]
    )

    print("\nAI RESPONSE\n")
    print(analysis)

else:
    print(result["message"])