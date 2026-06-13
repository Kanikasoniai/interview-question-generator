from fastapi import FastAPI, HTTPException
from questions import QUESTIONS
import random

app = FastAPI(
    title="Interview Question Generator",
    description="Generates interview questions for technical domains",
    version="1.0.0"
)

used_questions = {
    "python": set(),
    "data science": set(),
    "machine learning": set(),
    "web development": set()
}

DOMAIN_MAPPING = {
    "python": "python",
    "py": "python",

    "data science": "data science",
    "datascience": "data science",
    "ds": "data science",

    "machine learning": "machine learning",
    "ml": "machine learning",

    "web development": "web development",
    "web": "web development"
}


@app.get("/")
def home():
    return {
        "message": "Interview Question Generator API"
    }


@app.get("/domains")
def get_domains():
    return {
        "domains": list(QUESTIONS.keys())
    }


@app.get("/question/{domain}")
def generate_question(domain: str):

    normalized_domain = DOMAIN_MAPPING.get(
        domain.lower().strip()
    )

    if not normalized_domain:
        raise HTTPException(
            status_code=400,
            detail="Invalid domain"
        )

    available_questions = [
        q for q in QUESTIONS[normalized_domain]
        if q not in used_questions[normalized_domain]
    ]

    if not available_questions:
        used_questions[normalized_domain].clear()
        available_questions = QUESTIONS[normalized_domain]

    question = random.choice(available_questions)

    used_questions[normalized_domain].add(question)

    return {
        "domain": normalized_domain,
        "question": question
    }