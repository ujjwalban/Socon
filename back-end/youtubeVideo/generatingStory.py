import os
import openai
from openai import AzureOpenAI

def generate_story(topic,api_key,endpoint):
    api_base = endpoint
    api_key= api_key
    deployment_name = 'gpt-4'
    api_version = '2024-10-21'

    client = AzureOpenAI(
        api_key=api_key,  
        api_version=api_version,
        base_url=f"{api_base}/openai/deployments/{deployment_name}"
    )

    prompt = f"Create a concise, sophisticated script for a 30-second faceless YouTube Short on the topic '${topic}'. No visual or production notes needed—focus purely on engaging, spoken narrative."
    response = client.chat.completions.create(
        model="gpt-4",  # or "gpt-4" if you have access
        messages=[
            {"role": "user", "content": prompt}
        ],
        max_tokens=3000,
        temperature=0.7  # Adjust for creativity
    )
    return response.choices[0].message.content

def generate_story_for_voice(topic,api_key,endpoint):
    api_base = endpoint
    api_key= api_key
    deployment_name = 'gpt-4'
    api_version = '2024-10-21'

    client = AzureOpenAI(
        api_key=api_key,  
        api_version=api_version,
        base_url=f"{api_base}/openai/deployments/{deployment_name}"
    )
    prompt = f"remove all tone descripiton and act description in ${topic} so that TTS can work properly.Content should remain same."
    response = client.chat.completions.create(
        model="gpt-4",  # or "gpt-4" if you have access
        messages=[
            {"role": "user", "content": prompt}
        ],
        max_tokens=3000,
        temperature=0.7  # Adjust for creativity
    )
    return response.choices[0].message.content