from app.config import client
from app.utils.json_parser import extract_json


def estimate_time(tasks: list[str], total_days: int) -> dict:
    prompt = f"""
You are a project planning expert.

Tasks:
{tasks}

Total available time: {total_days} days

Distribute the total days across tasks realistically.

Return ONLY valid JSON in this exact format:
{{ "task name": number_of_days }}

Ensure total days equals {total_days}.
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
