import ffmpeg
import os

input_video = 'input/video.mkv'
output_audio = 'output/audio.mp3'

# Ensure output directory exists
os.makedirs(os.path.dirname(output_audio), exist_ok=True)

# Run ffmpeg command
ffmpeg.input(input_video).output(output_audio, **{'q:a': 0, 'map': 'a'}).run()

print(f"Audio successfully extracted to: {output_audio}")