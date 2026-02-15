from app.config import client


def run_task_decomposer(goal: str, days: int) -> list[str]:
    prompt = f"""
You are an expert project planner.

Goal: {goal}
Time available: {days} days

Break this goal into a clear list of actionable subtasks.
Return ONLY a bullet list. No explanations.
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": "You are a task planning assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.2,
    )

    text = response.choices[0].message.content

    tasks = [
        line.lstrip("-•0123456789. ").strip()
        for line in text.split("\n")
        if line.strip()
    ]

    return tasks
