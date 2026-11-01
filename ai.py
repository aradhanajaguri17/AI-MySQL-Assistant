from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

DATABASE_SCHEMA = """
Database: ai_assistant

students:
- id INT
- name VARCHAR
- age INT
- gender VARCHAR
- course VARCHAR
- year INT
- city VARCHAR
- email VARCHAR
- marks DECIMAL
"""

def generate_sql(question):
    prompt = f"""
You are a SQL assistant.

Convert the user's question into a MySQL SQL query.

Database schema:
{DATABASE_SCHEMA}

Rules:
- Generate ONLY SELECT queries.
- Never generate INSERT, UPDATE, DELETE, DROP, ALTER or CREATE.
- Return only SQL.
- Do not use markdown.
- Use MySQL syntax.

User question:
{question}
"""

    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    return response.choices[0].message.content.strip()


def generate_answer(question, result):
    prompt = f"""
You are a helpful database assistant.

User question:
{question}

Database result:
{result}

Give a simple natural-language answer.
Do not invent information.
Use only the provided database result.
"""

    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    return response.choices[0].message.content.strip()
