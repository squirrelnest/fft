import librosa
import numpy as np
import math

np.set_printoptions(legacy='1.25')

# Load audio file
audio_file = '/Users/surfista/Desktop/capsule-stl-main/media/come-together.mp3'  # Replace with your audio file path

# Process audio: y is time series, sr is sampling rate
y, sr = librosa.load(audio_file) 

# Detect beats
tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr, units="time", sparse=True, trim=True)

# Calculate time per sample in milliseconds
time_per_sample_ms = (1 / sr) * 1000

# Normalize the audio to range 0 to 1
normalized_y = ((y - np.min(y)) / (np.max(y) - np.min(y)))

# print("Sample Rate:", sr)

# Generate amplitude at each timeframe
amp_list = []

for i, amplitude in enumerate(normalized_y):
    time_ms = i * time_per_sample_ms
    # drop samples
    if round(time_ms) % 250 == 0:
        amp_list.append( [round(time_ms), round(amplitude, 4)] )
    
# Get last sample per set to avoid duplicate keyframes
# print(amp_list[::12])

# print("Sample Rate:", sr)
beat_list = []

# for i, beat in enumerate(beat_frames):
#     time_ms = i * time_per_sample_ms
#     # drop samples
#     if round(time_ms) % 250 == 0:
#         beat_list.append( [round(time_ms), round(beat, 4)] )
    
# print(beat_list)

# print("beat_timestamps: ", librosa.frames_to_time(beat_frames, sr=sr))

for i, beat in enumerate(beat_frames):
    beat_list.append(math.ceil(beat*1000))

print(beat_list)