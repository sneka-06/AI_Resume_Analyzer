from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(
    api_key=os.getenv("Groq_API")
)

def analyze_resume(text):
    try: 
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": f"Analyze this resume:\n{text}"
                }
            ]
        )
        return response.choices[0].message.content

    except Exception as e:
        return f"Error: {str(e)}" 