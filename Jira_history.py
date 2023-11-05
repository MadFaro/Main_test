
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

# Извлекаем результаты из левого и правого каналов
left_result = left_channel_output_data["result"]
right_result = right_channel_output_data["result"]

# Объединяем результаты из обоих каналов
merged_result = []

i, j = 0, 0

while i < len(left_result) and j < len(right_result):
    left_word = left_result[i]
    right_word = right_result[j]

    # Проверяем, совпадают ли слова по времени
    if left_word["start"] == right_word["end"]:
        merged_result.append(left_word["word"])
        merged_result.append(right_word["word"])
        i += 1
        j += 1
    elif left_word["start"] < right_word["end"]:
        merged_result.append(left_word["word"])
        i += 1
    else:
        merged_result.append(right_word["word"])
        j += 1

# Добавляем оставшиеся слова из левого и правого каналов
while i < len(left_result):
    merged_result.append(left_result[i]["word"])
    i += 1

while j < len(right_result):
    merged_result.append(right_result[j]["word"])
    j += 1

# Создаем предложение из объединенных результатов
sentence = " ".join(merged_result)

# Выводим предложение
print(sentence)
print(dialog)
