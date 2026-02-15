from typing import List, Dict


def build_day_wise_plan(plan: List[Dict]) -> Dict[str, List[str]]:
    """
    Converts task estimates into a day-wise schedule.
    """
    schedule = {}
    current_day = 1

    for item in plan:
        task = item["task"]
        duration = item["estimated_days"]

        for _ in range(duration):
            day_key = f"Day {current_day}"
            schedule.setdefault(day_key, []).append(task)
            current_day += 1

    return schedule
