import json
import requests
import openai
from openai import AzureOpenAI


def generate_topic_for_video(endpoint,gemini_api_key,openai_api_key):
    url = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent'
    headers = {
        'Content-Type': 'application/json',
    }
    payload = {
        "contents": [
            {
                "parts": [
                    {
                        "text":"Suggest a single, trending, and engaging one-line topic for a faceless YouTube video in one of the following: Bitcoin and its tech behind it.Focus on creating a topic based on the latest popular search trends that captures viewers' interest and curiosity."
                    }
                ]
            }
        ]
    }

    params = {'key': gemini_api_key}

    response = requests.post(url, headers=headers, params=params, data=json.dumps(payload))

    if response.status_code == 200:
        generated_topic = response.json()['candidates'][0]['content']['parts'][0]['text']

        return generated_topic
    else:
        api_base = endpoint
        api_key= openai_api_key
        deployment_name = 'gpt-4'
        api_version = '2024-10-21'

        client = AzureOpenAI(
            api_key= api_key,
            api_version= api_version,
            base_url=f"{api_base}/openai/deployments/{deployment_name}"
        )

        prompt = "Suggest a single, trending, and engaging one-line topic for a faceless YouTube video in one of the following: Bitcoin and its price prediction it.Focus on creating a topic based on the latest popular search trends that captures viewers' interest and curiosity."
        response = client.chat.completions.create(
            model="gpt-4",  # or "gpt-4" if you have access
            messages=[
                {"role": "user", "content": prompt}
            ],
            max_tokens=3000,
            temperature=0.7  # Adjust for creativity
        )
        return response.choices[0].message.content