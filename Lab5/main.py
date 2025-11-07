import soundfile as sf
import numpy as np

def process_audio(input_file):
    data, samplerate = sf.read(input_file)

    if len(data.shape) > 1: 
        data = np.mean(data, axis=1)
    
    print(data)

process_audio("Lab5/input.wav")