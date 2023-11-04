
ffmpeg -i test.wav -filter:a loudnorm -ar 8000 -c:a pcm_s16le test2.wav
ffmpeg -i test.wav -filter:a loudnorm -ar 8000 -c:a pcm_s16le -b:a 128k -ac 2 test2.wav
ffmpeg -i test2.wav -af "volume=3.5" test3.wav
ffmpeg -i test3.wav -filter:a "atempo=0.95" test4.wav


ffmpeg -i input.wav -ar 16000 output.wav
ffmpeg -i output.wav -af "highpass=f=300, lowpass=f=3000" output1.wav
ffmpeg -i output1.wav -af "volume=1.5" output2.wav
ffmpeg -i output2.wav -af "equalizer=f=1000:width_type=h:w=200:g=5" output3.wav
ffmpeg -i output3.wav -af "crystalizer" output4.wav
=ЕСЛИОШИБКА((((@Agents($AH$2;$AI$2;I18;I68)/30)*22,5)/0,85)/I166;2)

pip install pyspellchecker

from spellchecker import SpellChecker

# Создайте экземпляр класса SpellChecker
spell = SpellChecker()

# Ваш текст для проверки
text = "Пример текста с орфографическими ошибками. Я здесь чекаю спелл чекер."

# Разделите текст на слова
words = text.split()

# Найдите и исправьте опечатки
corrected_text = []
for word in words:
    corrected_word = spell.correction(word)
    corrected_text.append(corrected_word)

# Преобразуйте исправленные слова обратно в текст
corrected_text = " ".join(corrected_text)

# Выведите исправленный текст
print(corrected_text)

