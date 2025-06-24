import librosa
import numpy as np
import math

def get_beats(audio_file):

    # Set print option for floats
    np.set_printoptions(legacy='1.25')

    # Load and process audio: y is time series, sr is sampling rate
    y, sr = librosa.load(audio_file) 

    # Detect beats
    tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr, units="time", sparse=True, trim=True)

    # print("Tempo:", tempo)

    beat_list = []

    # print("beat_timestamps: ", librosa.frames_to_time(beat_frames, sr=sr))

    for i, beat in enumerate(beat_frames):
        beat_list.append(math.ceil(beat*1000))

    print(beat_list)

get_beats("/Users/surfista/Desktop/capsule-stl-main/media/higher-love.mp3")