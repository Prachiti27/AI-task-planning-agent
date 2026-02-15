import json
import re


def extract_json(text: str) -> dict:
    """
    Extract the first JSON object found in text.
    """
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass

    match = re.search(r"\{[\s\S]*\}", text)
    if match:
        try:
            return json.loads(match.group())
        except json.JSONDecodeError:
            pass

    raise ValueError("Failed to extract valid JSON from LLM response")
