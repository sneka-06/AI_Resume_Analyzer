from fastapi import FastAPI, UploadFile, File
from src.pdf_extractor import extract_text
from src.analyzer import analyze_resume
import tempfile
import os

app = FastAPI(
    title="AI Resume Analyzer"
)


@app.get("/")
def home():
    return {
        "message": "AI Resume Analyzer API Running"
    }


@app.post("/analyze")
async def analyze(file: UploadFile = File(...)):

    try:

        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".pdf"
        ) as temp_file:

            temp_file.write(await file.read())
            temp_path = temp_file.name

        extraction_result = extract_text(temp_path)

        os.remove(temp_path)

        if not extraction_result["success"]:
            return {
                "success": False,
                "error": extraction_result["message"]
            }

        analysis = analyze_resume(
            extraction_result["text"]
        )

        return {
            "success": True,
            "filename": file.filename,
            "analysis": analysis
        }

    except Exception as e:

        return {
            "success": False,
            "error": str(e)
        }