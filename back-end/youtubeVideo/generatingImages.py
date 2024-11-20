
import openai
import requests
import os
import json
from generatePromptForImage import generate_prompt_for_image
from openai import AzureOpenAI

def generate_images_for_scenes(story, api_key,endpoint):
   
    client = AzureOpenAI(
        api_version="2024-10-21",  
        api_key=api_key,   
        base_url=f"{endpoint}/openai/deployments/dall-e-3"
    )

    scenes = story.split('\n')  
    image_files = []
    
    output_folder = "scenes_images"
    os.makedirs(output_folder, exist_ok=True)

    for idx, scene in enumerate(scenes):
        if len(scene.strip()) > 0:  # Skip empty lines
            try:
                prompt_for_image = "Generate Real image" + generate_prompt_for_image(scene, api_key,endpoint)
                response = client.images.generate(
                    model = "dall-e-3",
                    prompt=prompt_for_image,
                    n=1,
                    size="1024x1024"
                )
                image_url = json.loads(response.model_dump_json())['data'][0]['url']
                image_file = os.path.join(output_folder, f"scene_{idx}.png")
                
                # Download and save the image using requests
                image_data = requests.get(image_url).content
                with open(image_file, 'wb') as f:
                    f.write(image_data)
                
                image_files.append(image_file)
            except Exception as e:
                print(f"Error generating image for scene {idx}: {e}")

    return image_files
