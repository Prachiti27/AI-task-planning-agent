def generate_markdown(goal: str, schedule: dict) -> str:
    md = f"# Goal: {goal}\n\n"

    for day, tasks in schedule.items():
        md += f"## {day}\n"
        for task in tasks:
            md += f"- [ ] {task}\n"
        md += "\n"

    return md
