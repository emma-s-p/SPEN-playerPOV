# -*- coding: utf-8 -*-
"""
Created on Wed Jul 30 01:44:07 2025
Converts files from HEVC to .mp4 and .wav files. it will also convert .mp4
files in to .wav files to be used with the TimeSync.m file
@author: Emma Paulson
"""

from moviepy.editor import VideoFileClip

def convert_hevc_to_mp4(input_path, output_path):
    """
    Converts an HEVC video to MP4 using MoviePy.
    
    This section of code is from a sample of how to use ffmpeg from 
    AI Overview a source for the code was not provided. The direct serch used
    was 'how to convert hevc to mp4 in python code using moviepy'
    """
    try:
        clip = VideoFileClip(input_path)
        clip.write_videofile(output_path, codec="libx264") # Specify H.264 codec
        print(f"Successfully converted '{input_path}' to '{output_path}'")
    except Exception as e:
        print(f"Error during conversion: {e}")

def convert_mp4_to_wav(input_mp4_path, output_wav_path):
    """
    Converts an MP4 video file to a WAV audio file.

    Args:
        input_mp4_path (str): The path to the input MP4 file.
        output_wav_path (str): The path where the output WAV file will be saved.
    """
    try:
        video_clip = VideoFileClip(input_mp4_path)
        audio_clip = video_clip.audio
        audio_clip.write_audiofile(output_wav_path, codec='pcm_s16le')
        audio_clip.close()
        video_clip.close()
        print(f"Conversion successful: '{input_mp4_path}' to '{output_wav_path}'")
    except Exception as e:
        print(f"Error during conversion: {e}")
        
#Get the file path for the video to be analyzed, and where the video will be 
#stored
print("PLEASE CHECK THAT THERE ARE NO QUOTES IN YOUR FILE PATH NAME")
input_video = input('video file path: ') #make sure that there are no quotes in the filepath name
output_file = input('chosen file name: ') # Desired output file name
output_video = output_file + '.mp4'
output_audio = output_file + '.wav'

convert_hevc_to_mp4(input_video, output_video)
convert_mp4_to_wav(output_video, output_audio)
