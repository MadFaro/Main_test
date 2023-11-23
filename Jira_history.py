
ffmpeg -i test.wav -filter:a loudnorm -ar 8000 -c:a pcm_s16le test2.wav
ffmpeg -i test.wav -filter:a loudnorm -ar 8000 -c:a pcm_s16le -b:a 128k -ac 2 test2.wav
ffmpeg -i test2.wav -af "volume=3.5" test3.wav
ffmpeg -i test3.wav -filter:a "atempo=0.95" test4.wav
ffmpeg -i input.wav -ar 16000 output.wav
ffmpeg -i output.wav -af "highpass=f=300, lowpass=f=3000" output1.wav
ffmpeg -i output1.wav -af "volume=1.5" output2.wav
ffmpeg -i output2.wav -af "equalizer=f=1000:width_type=h:w=200:g=5" output3.wav
ffmpeg -i output3.wav -af "crystalizer" output4.wav

from razdel import tokenize
import pymorphy2

def normalize_text(text):
    morph = pymorphy2.MorphAnalyzer()
    tokens = [morph.parse(token.text.lower())[0].normal_form for token in tokenize(text)]
    return ' '.join(tokens)

def search_phrases_and_derivatives(text, phrases):
    normalized_text = normalize_text(text)
    results = []

    for phrase in phrases:
        normalized_phrase = normalize_text(phrase)
        if normalized_phrase in normalized_text:
            results.append(phrase)

    return results

text_to_search = "не перебивай меня. перебивай его. Перебивайте меня, если что-то не так."
phrases_to_search = ["не перебивайте", "что-то не так"]

search_result = search_phrases_and_derivatives(text_to_search, phrases_to_search)

print("Найденные совпадения:", search_result)

