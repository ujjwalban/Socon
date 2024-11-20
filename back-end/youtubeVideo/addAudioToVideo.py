import os
from moviepy.editor import VideoFileClip, AudioFileClip

def add_audio_to_video(audio_file, video_file, output_folder="final_videos", output_file="final_output.mp4"):
    os.makedirs(output_folder, exist_ok=True)
    
    output_path = os.path.join(output_folder, output_file)
    
    video_clip = VideoFileClip(video_file)
    audio_clip = AudioFileClip(audio_file)
    
    final_video = video_clip.set_audio(audio_clip)
    
    final_video.write_videofile(output_path, codec="libx264", audio_codec="aac")
    
    absolute_path_for_final_video = os.path.abspath(output_path)
    print(f"Audio added to the video successfully. Output file path: {absolute_path_for_final_video}")
    
    return absolute_path_for_final_video
