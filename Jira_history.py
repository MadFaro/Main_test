import vosk
import soundfile as sf
import numpy as np
import os
import concurrent.futures

model_path = r'vosk-model-ru-0.22'
audio_directory = 'audio/'
batch_size = 10  # Размер пакета для обработки

def load_audio_data(audio_file):
    audio_data, sample_rate = sf.read(audio_file)
    left_channel = audio_data[:, 0]
    left_channel_bytes = (left_channel * np.iinfo(np.int16).max).astype(np.int16).tobytes()
    return left_channel_bytes, sample_rate

def process_audio_batch(operator_batch, client_batch, model, sample_rate):
    operator_recognizer = vosk.KaldiRecognizer(model, sample_rate)
    client_recognizer = vosk.KaldiRecognizer(model, sample_rate)
    operator_text = []
    client_text = []
    
    for operator_audio, client_audio in zip(operator_batch, client_batch):
        operator_recognizer.AcceptWaveform(operator_audio)
        operator_result = operator_recognizer.Result()
        operator_text.append(operator_result["text"])
        
        client_recognizer.AcceptWaveform(client_audio)
        client_result = client_recognizer.Result()
        client_text.append(client_result["text"])
    
    return operator_text, client_text

def find_words(audio_files, model):
    results = []
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []
        operator_batch = []
        client_batch = []
        sample_rate = None
        for audio_file in audio_files:
            audio_data, sr = load_audio_data(audio_file)
            
            if sample_rate is None:
                sample_rate = sr
            
            if len(operator_batch) < batch_size:
                operator_batch.append(audio_data)
            else:
                client_batch.append(audio_data)
                
                if len(client_batch) == batch_size:
                    future = executor.submit(process_audio_batch, operator_batch, client_batch, model, sample_rate)
                    futures.append(future)
                    operator_batch = []
                    client_batch = []
        
        if operator_batch:
            future = executor.submit(process_audio_batch, operator_batch, client_batch, model, sample_rate)
            futures.append(future)
            
        for future in concurrent.futures.as_completed(futures):
            operator_text, client_text = future.result()
            results.append((operator_text, client_text))
    return results

if __name__ == '__main__':
    model = vosk.Model(model_path)
    audio_files = [os.path.join(audio_directory, filename) for filename in os.listdir(audio_directory) if filename.endswith('.wav')]
    found_words = find_words(audio_files, model)
    for operator_text, client_text in found_words:
        for operator_phrase, client_phrase in zip(operator_text, client_text):
            print(f"- Оператор: {operator_phrase}")
            print(f"- Клиент: {client_phrase}")
