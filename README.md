# Interview Question Generator

## Overview

Interview Question Generator is a FastAPI-based REST API that generates technical interview questions from predefined domains.

The project was developed to automate interview question generation while handling duplicate questions and incorrect domain mappings.

---

## Objective

Generate relevant interview questions for the following domains:

* Python
* Data Science
* Machine Learning
* Web Development

The API returns responses in JSON format.

Example:

```json
{
  "domain": "machine learning",
  "question": "Explain overfitting in Machine Learning."
}
```

---

## Features

* Generate domain-specific interview questions
* REST API built using FastAPI
* JSON response format
* Duplicate question prevention
* Domain alias support
* Error handling for invalid domains
* Interactive Swagger API documentation

---

## Supported Domains

| Domain           | Aliases                       |
| ---------------- | ----------------------------- |
| Python           | python, py                    |
| Data Science     | data science, datascience, ds |
| Machine Learning | machine learning, ml          |
| Web Development  | web development, web          |

---

## Project Structure

```text
interview-question-generator/
│
├── app.py
├── questions.py
├── requirements.txt
├── README.md
├── .gitignore
└── venv/
```

---

## Installation

### Clone Repository

```bash
git clone <repository-url>
cd interview-question-generator
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run Application

```bash
uvicorn app:app --reload
```

Server:

```text
http://127.0.0.1:8000
```

Swagger Documentation:

```text
```
