# src/main.py

import os
import ffmpeg
from pydub import AudioSegment
from pyannote.audio import Pipeline

def extract_audio_from_video(video_file, output_audio_file):
    try:
        (
            ffmpeg
            .input(video_file)
            .output(output_audio_file)
            .run()
        )
        print(f"Audio extracted successfully to {output_audio_file}")
    except ffmpeg.Error as e:
        print(f"Error: {e}")

def diarize_audio(input_audio_file):
    pipeline = Pipeline.from_pretrained("pyannote/speaker-diarization")
    diarization = pipeline(input_audio_file)
    return diarization

def split_audio_by_speaker(input_audio_file, diarization):
    audio = AudioSegment.from_wav(input_audio_file)
    speaker_wavs = {}

    for turn, _, speaker in diarization.itertracks(yield_label=True):
        start_time = int(turn.start * 1000)  # in milliseconds
        end_time = int(turn.end * 1000)      # in milliseconds
        speaker_label = f"speaker_{speaker}"
        
        if speaker_label not in speaker_wavs:
            speaker_wavs[speaker_label] = AudioSegment.empty()
        
        speaker_wavs[speaker_label] += audio[start_time:end_time]

    for speaker, audio_segment in speaker_wavs.items():
        output_file = f"../data/{speaker}.wav"
        audio_segment.export(output_file, format="wav")
        print(f"Exported {speaker} audio to {output_file}")

if __name__ == "__main__":
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    input_video_path = os.path.join(project_root, 'data', 'input_video.mp4')
    output_audio_path = os.path.join(project_root, 'data', 'output_audio.wav')
    
    extract_audio_from_video(input_video_path, output_audio_path)
    
    diarization = diarize_audio(output_audio_path)
    
    split_audio_by_speaker(output_audio_path, diarization)
