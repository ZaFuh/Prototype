#Generate functional requirements as JSON

from openai import OpenAI
import json

def generate_functional_json(prompt):
    client = OpenAI()
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": f"Task: {prompt}. Return JSON describing goal, object, force, precision, object properties, grasp type."}],
        response_format={"type": "json_object"}
    )
    data = json.loads(response.choices[0].message.content)
    return data
