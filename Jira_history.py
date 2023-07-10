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

def check_phrases(text, phrases):
    tokens = nltk.word_tokenize(text)
    found_phrases = []
    for phrase in phrases:
        phrase_tokens = nltk.word_tokenize(phrase)
        if all(token in tokens for token in phrase_tokens):
            found_phrases.append(phrase)
    return found_phrases

def process_audio_files(audio_files, model, phrases):
    results = []
    for audio_file in audio_files:
        audio_data, sample_rate = load_audio_data(audio_file)
        recognizer = vosk.KaldiRecognizer(model, sample_rate)
        recognizer.AcceptWaveform(audio_data)
        result = recognizer.FinalResult()
        text = result['text']
        found_phrases = check_phrases(text, phrases)
        results.append({'audio_file': audio_file, 'text': text, 'found_phrases': found_phrases})
    return results

def find_words(audio_files, model, phrases, batch_size):
    results = []
    for i in range(0, len(audio_files), batch_size):
        batch_files = audio_files[i:i+batch_size]
        batch_results = process_audio_files(batch_files, model, phrases)
        results.extend(batch_results)
    return results

if __name__ == '__main__':
    model = vosk.Model(model_path)
    audio_files = [os.path.join(audio_directory, filename) for filename in os.listdir(audio_directory) if filename.endswith('.wav')]
    phrases = ["пример текста", "мы будем", "не найдена"]
    batch_size = 10
    found_words = find_words(audio_files, model, phrases, batch_size)
    print(found_words)
