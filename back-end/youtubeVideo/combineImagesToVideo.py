import os
from moviepy.editor import ImageSequenceClip, ImageClip, AudioFileClip
from moviepy.video.fx import all as vfx
from PIL import Image

def get_video_length(audio_file):
    """
    Get the duration of a video file.
    """
    audio = AudioFileClip(audio_file)
    return audio.duration


from moviepy.editor import ImageSequenceClip, AudioFileClip
import os

def get_audio_length(audio_file):
    """
    Get the duration of an audio file.
    """
    audio = AudioFileClip(audio_file)
    duration = audio.duration
    audio.close()  # Close the file to avoid resource issues
    return duration


def combine_images_into_video(frame_paths, audio_file, output_folder="videos", output_video="output_video.mp4"):
    """
    Combine image frames into a video with a specified duration based on the audio file.

    Args:
    - frame_paths (list): List of file paths to the image frames.
    - audio_file (str): Path to the audio file for calculating duration.
    - output_folder (str): Folder to save the output video.
    - output_video (str): Name of the output video file.

    Returns:
    - output_path (str): Path to the generated video file.
    """
    # Ensure the output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # Get audio duration
    total_duration = get_audio_length(audio_file)

    # Calculate frame duration to match total audio duration
    num_frames = len(frame_paths)
    fps = num_frames / total_duration  # Frames per second

    # Combine frames into a video
    output_path = os.path.join(output_folder, output_video)
    video_clip = ImageSequenceClip(frame_paths, fps=fps)

    # Add audio to the video
    video_clip = video_clip.set_audio(AudioFileClip(audio_file))

    # Write the video file to disk
    video_clip.write_videofile(output_path, codec="libx264")

    print(f"Video saved to {output_path}")
    return output_path

