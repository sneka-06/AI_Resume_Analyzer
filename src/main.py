import argparse
from pdf_extractor import extract_text
from analyzer import analyze_resume


def main():

    parser = argparse.ArgumentParser(
        description="AI Resume Analyzer"
    )

    parser.add_argument(
        "--resume",
        required=True,
        help="Path to resume PDF"
    )

    args = parser.parse_args()

    print("\nExtracting resume text...\n")

    result = extract_text(args.resume)

    if not result["success"]:
        print(f"Error: {result['message']}")
        return

    print("Analyzing resume...\n")

    analysis = analyze_resume(result["text"])

    if "error" in analysis:
        print(f"Error: {analysis['error']}")
        return

    print("=" * 50)
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


if __name__ == "__main__":
    main()