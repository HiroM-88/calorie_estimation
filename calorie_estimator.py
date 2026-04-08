import os 
import json
import requests
from dotenv import load_dotenv

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")


def estimate_calories(food_items):
    """
    Estimate calorie ranges for unique food itmes using an LLM.
    Returns a dict like:
    {
        "pizza": [250, 350],
        "cake:: [300, 450]
    }
    """

    unique_items = list(set(food_items))

    prompt = f"""
        Estimate a rough calorie range for each of the following food items in a typical serving:

        {", ".join(unique_items)}

        Return only valid JSON in this format:
        {{
            "pizza": [250, 350],
            "cake": [300, 450]
        }}

        Do not include any explanation.
    """

    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "openrouter/free",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant that estimates calorie ranges for food items."},
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post(url, headers=headers, json=payload, timeout=60)
    response.raise_for_status()

    result = response.json()
    content = result["choices"][0]["message"]["content"]

    # Convert JSON string to Python dict
    calorie_dict = json.loads(content)
    return calorie_dict

if __name__ == "__main__":
    test_items = ["pizza", "cake", "pizza", "sushi"]
    calorie_ranges = estimate_calories(test_items)
    print(calorie_ranges)