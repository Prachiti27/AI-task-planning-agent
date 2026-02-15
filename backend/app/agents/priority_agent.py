from app.config import client
from app.utils.json_parser import extract_json


def assign_priority(tasks: list[str]) -> dict:
    prompt = f"""
Tasks:
{tasks}

Assign a priority to each task.
Use ONLY: High, Medium, Low.

Return ONLY valid JSON in this format:
{{ "task name": "priority" }}

No explanations. No text.
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": "Return JSON only."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.2
    )

    text = response.choices[0].message.content
    return extract_json(text)
