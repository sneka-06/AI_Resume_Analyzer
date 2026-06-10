from groq import Groq
from dotenv import load_dotenv
import os
import json

# Load environment variables
load_dotenv()

# Initialize Groq client
client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def analyze_resume(text):
    """
    Analyze resume text and return structured JSON.
    """

    prompt = f"""
You are an ATS resume reviewer.

Analyze the following resume and return ONLY valid JSON.

Required format:

{{
    "strengths": [],
    "weaknesses": [],
    "missing_skills": [],
    "suggestions": []
}}

Rules:
- Return JSON only
- No markdown
- No explanations
- No extra text outside JSON

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

        # Handle cases where model wraps JSON in markdown
        if raw_output.startswith("```json"):
            raw_output = raw_output.replace("```json", "")
            raw_output = raw_output.replace("```", "")
            raw_output = raw_output.strip()

        parsed_output = json.loads(raw_output)

        return parsed_output

    except json.JSONDecodeError:
        return {
            "error": "Invalid JSON returned by model",
            "raw_response": raw_output
        }

    except Exception as e:
        return {
            "error": str(e)
        }