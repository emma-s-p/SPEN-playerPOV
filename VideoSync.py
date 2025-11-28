# -*- coding: utf-8 -*-
"""
Created on Thu Nov 27 17:17:21 2025

This code must be used in conjunction with the TimeSync MatLab Function. 

This code takes two video inputs, and using the results from the MatLab
TimeSync function, creates two .mp4 files that play the two input videos at
the same time where they are synced. Each of the output video files will have
the audio from one of the original videos. 

This code also produces the .wav files needed to run the MatLab TimeSync
function. Two additional .mp4 files are generated while running this code.
Those files can be deleted after the code has been exicuted. 

@author: Emma Paulson
"""
from moviepy.editor import VideoFileClip, clips_array

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

#get the file paths for the videos that are being compared
print("PLEASE CHECK THAT THERE ARE NO QUOTES IN YOUR FILE PATH NAME")
input_video1 = input('Longer Video file path: ')
output_file1 = input('chosen file name: ') # Desired output file
long_video = output_file1 + '.mp4'
long_audio = output_file1 + '.wav'

print("PLEASE CHECK THAT THERE ARE NO QUOTES IN YOUR FILE PATH NAME")
input_video2 = input('Shorter Video file path: ')
output_file2 = input('chosen file name: ') # Desired output file
short_video = output_file2 + '.mp4'
short_audio = output_file2 + '.wav'

final_file = input("Choose a final file name: ")

convert_hevc_to_mp4(input_video1, long_video)
convert_mp4_to_wav(input_video1, long_audio)

long_video = VideoFileClip(long_video)

convert_hevc_to_mp4(input_video2, short_video)
convert_mp4_to_wav(input_video2, short_audio)

short_video = VideoFileClip(short_video)

print("Run the MatLab TimeSync Function")
start_time = input("Input the MatLab results: ")
end = input("The short video length time: ")
end_time = float(start_time) + float(end)

clipped = long_video.subclip(start_time,end_time)
stacked = clips_array([[clipped],[short_video]])

audio1 = stacked.set_audio(clipped.audio)
audio1.write_videofile(final_file+"_audio1.mp4",codec="libx264", audio_codec="aac")
audio2 = stacked.set_audio(short_video.audio)
audio2.write_videofile(final_file+"_audio2.mp4",codec="libx264", audio_codec="aac")

long_video.close()
short_video.close()
clipped.close()
stacked.close()
audio1.close()
audio2.close()