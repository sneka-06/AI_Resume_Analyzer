from groq import Groq
from dotenv import load_dotenv
import os
import json

# Load environment variables
load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def analyze_resume(text):
    """
    Analyze resume and return structured JSON.
    """

    prompt = f"""
You are an ATS resume reviewer.

Analyze the resume and return ONLY valid JSON.

Format:

{{
    "score": 0,
    "score_breakdown": {{
        "skills": 0,
        "experience": 0,
        "education": 0,
        "resume_quality": 0
    }},
    "strengths": [],
    "weaknesses": [],
    "missing_skills": [],
    "suggestions": []
}}

Rules:
- Return ONLY JSON
- No markdown
- No explanations
- No comments
- No trailing characters
- The JSON must be parsable by Python json.loads()
- Score must be between 1 and 100
- score_breakdown values should approximately add up to the overall score

Resume:
{text}
"""

    try:

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        raw_output = response.choices[0].message.content.strip()

        # Remove markdown fences if present
        raw_output = raw_output.replace("```json", "")
        raw_output = raw_output.replace("```", "")
        raw_output = raw_output.strip()

        try:
            parsed_output = json.loads(raw_output)
            return parsed_output

        except json.JSONDecodeError:

            # Common cleanup for malformed responses
            raw_output = raw_output.replace(")}", "}")
            raw_output = raw_output.replace("\n", " ")

            parsed_output = json.loads(raw_output)

            return parsed_output

    except Exception as e:

        return {
            "error": str(e)
        }