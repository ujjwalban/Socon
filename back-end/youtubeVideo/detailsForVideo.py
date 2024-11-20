import os
import openai
from openai import AzureOpenAI



def generate_description(topic,api_key,endpoint):
    api_base = endpoint
    api_key= api_key
    deployment_name = 'gpt-4'
    api_version = '2024-10-21'

    client = AzureOpenAI(
    api_key=api_key,  
    api_version=api_version,
    base_url=f"{api_base}/openai/deployments/{deployment_name}"
    )
    prompt = f"Generate an SEO-optimized YouTube video description in bullet points for '${topic}' aimed at maximizing reach. Include high-impact keywords, a compelling summary of what viewers will gain, and key points that highlight unique insights or benefits. Structure the description to engage viewers and improve discoverability, making it both informative and inviting to encourage more clicks and views."
    response = client.chat.completions.create(
        model="gpt-4",  
        messages=[
            {"role": "user", "content": prompt}
        ],
        max_tokens=3000,
        temperature=0.7  
    )
    return response.choices[0].message.content
    


def generate_title(topic, api_key,endpoint):
    api_base = endpoint
    api_key= api_key
    deployment_name = 'gpt-4'
    api_version = '2024-10-21'

    client = AzureOpenAI(
    api_key=api_key,  
    api_version=api_version,
    base_url=f"{api_base}/openai/deployments/{deployment_name}"
    )
    prompt = f"Generate an engaging YouTube Shorts title up to 100 characters related to '${topic}'. The title should include relevant keywords and a strong hook (e.g., 'How to', 'Top 5', 'Must-see', or a question like 'Did you know?') to maximize reach and attract clicks. Make it specific and clear, avoiding generic phrases, so viewers know exactly what they’ll gain by watching."
    response = client.chat.completions.create(
        model="gpt-4", 
        messages=[
            {"role": "user", "content": prompt}
        ],
        max_tokens=1000,
        temperature=0.7  
    )
    return response.choices[0].message.content