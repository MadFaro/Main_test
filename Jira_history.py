<<<<<<< HEAD
﻿import vosk
import soundfile as sf
import numpy as np
import os
import concurrent.futures
import nltk
=======
>>>>>>> 5a99c49780f4d72714c4a0e85adf433fdafb12d8

ffmpeg -i test.wav -filter:a loudnorm -ar 8000 -c:a pcm_s16le test2.wav
ffmpeg -i test.wav -filter:a loudnorm -ar 8000 -c:a pcm_s16le -b:a 128k -ac 2 test2.wav
ffmpeg -i test2.wav -af "volume=3.5" test3.wav
ffmpeg -i test3.wav -filter:a "atempo=0.95" test4.wav


<<<<<<< HEAD
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
=======
ffmpeg -i input.wav -ar 16000 output.wav
ffmpeg -i output.wav -af "highpass=f=300, lowpass=f=3000" output1.wav
ffmpeg -i output1.wav -af "volume=1.5" output2.wav
ffmpeg -i output2.wav -af "equalizer=f=1000:width_type=h:w=200:g=5" output3.wav
ffmpeg -i output3.wav -af "crystalizer" output4.wav
=ЕСЛИОШИБКА((((@Agents($AH$2;$AI$2;I18;I68)/30)*22,5)/0,85)/I166;2)


from seleniumwire import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService


driver = webdriver.Chrome()
driver.get('https://www.google.com/')

SELECT TRUNC(SYSDATE, 'HH24') + (FLOOR((TO_NUMBER(TO_CHAR(SYSDATE, 'MI')) / 30)) * (1/48)) AS rounded_date
FROM dual;
>>>>>>> 5a99c49780f4d72714c4a0e85adf433fdafb12d8
