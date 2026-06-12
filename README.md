# AI Resume Analyzer

An AI-powered Resume Analyzer built using Python, Groq LLM, FastAPI, SQLite, and PyPDF.

## Features

* Upload resume PDFs
* Extract text from resumes
* Analyze resumes using AI
* Generate ATS score (1-100)
* Provide strengths and weaknesses
* Suggest missing skills
* Store analysis history in SQLite
* REST API built with FastAPI

## Tech Stack

* Python
* FastAPI
* Groq LLM
* SQLite
* PyPDF
* Uvicorn

## Project Structure

```text
ai_resume_analyzer/
├── src/
├── tests/
├── resumes/
├── README.md
└── requirements.txt
```

## Installation

```bash
git clone <repo-url>
cd ai_resume_analyzer

pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_api_key
```

## Run API

```bash
uvicorn src.main:app --reload
```

Open:

http://127.0.0.1:8000/docs

## Example Response

```json
{
  "score": 85,
  "strengths": [
    "Business Strategy",
    "Project Management"
  ],
  "weaknesses": [
    "Limited Technical Skills"
  ]
}
```

## Future Improvements

* Job description matching
* Resume keyword optimization
* Multi-resume comparison
* Cloud deployment on AWS

