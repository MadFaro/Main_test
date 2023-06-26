import vosk
import soundfile as sf
import numpy as np

model_path = r'C:\Users\TologonovAB\Desktop\audio_totext\vosk-model-ru-0.22'
audio_file = 'audio\\audio.wav'

def find_words(audio_file , model_path):
    audio_data, sample_rate = sf.read(audio_file)
    left_channel = audio_data[:, 0]
    #left_channel_bytes = (left_channel * np.iinfo(np.int16).max).astype(np.int16).tobytes()
    sf.write('audio\\audio2.wav', left_channel, samplerate=sample_rate)
    with open('audio\\audio2.wav', 'rb') as file:
        data = file.read()

    model = vosk.Model(model_path)
    recognizer = vosk.KaldiRecognizer(model, sample_rate)
    recognizer.AcceptWaveform(data)
    result = recognizer.FinalResult()

    return result

found_words = find_words(audio_file=audio_file, model_path=model_path)

print(found_words)
