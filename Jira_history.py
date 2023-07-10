import vosk
import soundfile as sf
import numpy as np
import os
import concurrent.futures
import nltk

model_path = r'vosk-model-ru-0.22'
audio_directory = 'audio/'

def load_audio_data(audio_file):
    audio_data, sample_rate = sf.read(audio_file)
    left_channel = audio_data[:, 0]
    left_channel_bytes = (left_channel * np.iinfo(np.int16).max).astype(np.int16).tobytes()
    return left_channel_bytes, sample_rate

def process_audio_file(audio_file, model, phrases):
    audio_data, sample_rate = load_audio_data(audio_file)
    recognizer = vosk.KaldiRecognizer(model, sample_rate)
    recognizer.AcceptWaveform(audio_data)
    result = recognizer.FinalResult()
    text = result['text']
    check_phrases(text, phrases)
    return {'audio_file': audio_file, 'text': text, 'found_phrases': check_phrases(text, phrases)}

def find_words(audio_files, model, phrases):
    results = []
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []
        for audio_file in audio_files:
            future = executor.submit(process_audio_file, audio_file, model, phrases)
            futures.append(future)
        for future in concurrent.futures.as_completed(futures):
            result = future.result()
            results.append(result)
    return results

if __name__ == '__main__':
    model = vosk.Model(model_path)
    audio_files = [os.path.join(audio_directory, filename) for filename in os.listdir(audio_directory) if filename.endswith('.wav')]
    phrases = ["пример текста", "мы будем", "не найдена"]
    found_words = find_words(audio_files, model, phrases)
    print(found_words)
