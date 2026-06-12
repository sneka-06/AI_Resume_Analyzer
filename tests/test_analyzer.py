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

    if "error" in analysis:

        print("\nERROR")
        print(analysis)

    else:

        print("\n" + "=" * 50)
        print("ATS SCORE")
        print("=" * 50)

        print(analysis["score"])

        print("\n" + "=" * 50)
        print("SCORE BREAKDOWN")
        print("=" * 50)

        for category, score in analysis["score_breakdown"].items():
            print(f"{category}: {score}")

        print("\n" + "=" * 50)
        print("STRENGTHS")
        print("=" * 50)

        for item in analysis["strengths"]:
            print("-", item)

        print("\n" + "=" * 50)
        print("WEAKNESSES")
        print("=" * 50)

        for item in analysis["weaknesses"]:
            print("-", item)

        print("\n" + "=" * 50)
        print("MISSING SKILLS")
        print("=" * 50)

        for item in analysis["missing_skills"]:
            print("-", item)

        print("\n" + "=" * 50)
        print("SUGGESTIONS")
        print("=" * 50)

        for item in analysis["suggestions"]:
            print("-", item)

else:

    print(result["message"])