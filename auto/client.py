import os
import json
import requests

BASE_URL = os.environ.get('OLLAMA_HOST', 'http://localhost:11434')


def generate(model_name, prompt, system=None, template=None, context=None,
             options=None):
    try:
        url = f"{BASE_URL}/api/generate"
        payload = {
            "model": model_name,
            "prompt": prompt,
            "system": system,
            "template": template,
            "context": context,
            "options": options
        }
        # Remove keys with None values
        payload = {k: v for k, v in payload.items() if v is not None}
        with requests.post(url, json=payload, stream=True) as response:
            response.raise_for_status()
            # Variable to hold concatenated response strings if no callback
            # is provided
            full_response = ""

            for line in response.iter_lines():
                if line:
                    chunk = json.loads(line)
                    if not chunk.get("done"):
                        response_piece = chunk.get("response", "")
                        full_response += response_piece
            # Return the full response and the final context
            return full_response.strip()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
