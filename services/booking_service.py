import json
import re
import ollama


def extract_booking_info(user_message: str):

    prompt = f"""
Extract booking information from the text.

Return ONLY JSON.

Example:

{{
    "name": "",
    "email": "",
    "date": "",
    "time": ""
}}

Text:
{user_message}
"""

    response = ollama.chat(
        model="llama3",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    content = response["message"]["content"]

    print("RAW RESPONSE:")
    print(content)

    try:
        match = re.search(
            r"\{.*\}",
            content,
            re.DOTALL
        )

        if not match:
            return None

        return json.loads(
            match.group()
        )

    except Exception as e:
        print("JSON ERROR:", e)
        return None