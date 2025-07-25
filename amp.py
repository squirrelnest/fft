import librosa
import numpy as np
import math

def get_amps(audio_file):

    # Set print options for floats
    np.set_printoptions(legacy='1.25')

    # Load and process audio: y is time series, sr is sampling rate
    y, sr = librosa.load(audio_file) 

    # Calculate time per sample in milliseconds
    time_per_sample_ms = (1 / sr) * 1000

    # Normalize the audio to range 0 to 1
    normalized_y = ((y - np.min(y)) / (np.max(y) - np.min(y)))

    # Print sample rate
    # print("Sample Rate:", sr)

    # Generate amplitude at each timeframe
    amp_list = []

    for i, amplitude in enumerate(normalized_y):
        time_ms = i * time_per_sample_ms
        # drop samples
        if round(time_ms) % 250 == 0:
            amp_list.append( [round(time_ms), round(amplitude, 4)] )
        
    # Get last sample per set to avoid duplicate keyframes
    print(amp_list[::12])

get_amps("/Users/surfista/Desktop/capsule-stl-main/media/come-together.mp3")