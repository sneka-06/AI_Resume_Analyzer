import sqlite3


DATABASE_NAME = "resume_analyzer.db"


def get_connection():
    return sqlite3.connect(DATABASE_NAME)

def create_table():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS analyses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        filename TEXT,
        analysis_date TEXT,
        strengths TEXT,
        weaknesses TEXT,
        missing_skills TEXT,
        suggestions TEXT
    )
    """)

    conn.commit()
    conn.close()

import json


def save_analysis(filename, analysis):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO analyses (
        filename,
        analysis_date,
        strengths,
        weaknesses,
        missing_skills,
        suggestions
    )
    VALUES (?, datetime('now'), ?, ?, ?, ?)
    """,
    (
        filename,
        json.dumps(analysis["strengths"]),
        json.dumps(analysis["weaknesses"]),
        json.dumps(analysis["missing_skills"]),
        json.dumps(analysis["suggestions"])
    ))

    conn.commit()
    conn.close()

def get_history():

    conn = get_connection()

    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()

    cursor.execute("""
    SELECT *
    FROM analyses
    ORDER BY id DESC
    """)

    rows = cursor.fetchall()

    conn.close()

    return [dict(row) for row in rows]