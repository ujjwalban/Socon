import os
import generatingTopic
import generatingStory
from moviepy.editor import *
from generatingAudio import synthesize_speech
from generatingImages import generate_images_for_scenes
from combineImagesToVideo import combine_images_into_video
from addAudioToVideo import add_audio_to_video
from uploadingYoutubeVideo import authenticate_youtube, upload_video
from detailsForVideo import generate_description,generate_title
from uploadingYoutubeShorts import authenticate_youtube, upload_shorts
from generatingZoomEffects import zoom_in_and_out_frames
from dotenv import load_dotenv

# Complete Workflow Example:
if __name__ == "__main__":

    load_dotenv()

    gemini_api_key = os.getenv('GEMINI_API_KEY')
    openai_api_endpoint = os.getenv('OPENAI_API_ENDPOINT')
    openai_api_key = os.getenv('OPENAI_API_KEY')
    dalle_api_key = os.getenv('DALLE_API_KEY')

    topic = generatingTopic.generate_topic_for_video(openai_api_endpoint,openai_api_key)
    print("Generated Topic:", topic)

    story_text = generatingStory.generate_story_for_voice(generatingStory.generate_story(topic, openai_api_key,openai_api_endpoint),openai_api_key,openai_api_endpoint)

    print(f"Generated Story: {story_text}")

    # Step 2: Synthesize narration using Google Cloud TTS
    narration_file = synthesize_speech(story_text, output_file="voice.mp3")

    # Step 3: Generate images for each scene in the story
    images = generate_images_for_scenes(story_text,openai_api_key,openai_api_endpoint)

    frame_paths = zoom_in_and_out_frames(images,"zoom_in_frames",5)

    # Step 4: Combine images into a video
    video_file = combine_images_into_video(frame_paths, narration_file, output_folder="videos", output_video="final_video.mp4")
    absolute_path = os.path.abspath(video_file)
    print(f'Output file path: {absolute_path}')

    # Step 5: Add narration (audio) to the video
    final_video = add_audio_to_video(narration_file, video_file)
    youtube = authenticate_youtube()
    tags = [
    "Trending", "Top 10", "How To", "Must Watch", "Did You Know", 
    "Tips and Tricks", "Life Hacks", "2024 Trends", "Learn Something New", 
    "DIY", "Inspiration", "For Beginners", "Expert Advice", 
    "Top Facts", "Mind Blowing", "Insider Tips", "Step by Step", 
    "Quick Guide", "Motivation", "Surprising Facts"
    ]

    title = generate_title(topic,openai_api_key,openai_api_endpoint)
    print('----------------------------------------------------')
    print(f'Title: {title}')
    print('----------------------------------------------------')
    description  = generate_description(topic,openai_api_key,openai_api_endpoint)
    print('----------------------------------------------------')
    print(f'Description: {description}')
    print('----------------------------------------------------')

    upload_shorts(youtube, final_video, title, description, tags, 28)
 #   upload_video(youtube, final_video, title, description, tags, 28)

