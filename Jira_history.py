
ffmpeg -i test.wav -filter:a loudnorm -ar 8000 -c:a pcm_s16le test2.wav
ffmpeg -i test.wav -filter:a loudnorm -ar 8000 -c:a pcm_s16le -b:a 128k -ac 2 test2.wav
ffmpeg -i test2.wav -af "volume=3.5" test3.wav
ffmpeg -i test3.wav -filter:a "atempo=0.95" test4.wav
ffmpeg -i input.wav -ar 16000 output.wav
ffmpeg -i output.wav -af "highpass=f=300, lowpass=f=3000" output1.wav
ffmpeg -i output1.wav -af "volume=1.5" output2.wav
ffmpeg -i output2.wav -af "equalizer=f=1000:width_type=h:w=200:g=5" output3.wav
ffmpeg -i output3.wav -af "crystalizer" output4.wav

# Разбираем строки в JSON
left_channel_output_data = json.loads(left_channel_output_str)
right_channel_output_data = json.loads(right_channel_output_str)

# Извлекаем результаты из левого и правого каналов
left_result = left_channel_output_data["result"]
right_result = right_channel_output_data["result"]

# Создаем словарь для идентификации говорящего
speaker_mapping = {
    "left": "Оператор",
    "right": "Клиент"
}

# Объединяем результаты из обоих каналов с информацией о говорящем
merged_result = []

i, j = 0, 0
current_speaker = "left"

while i < len(left_result) and j < len(right_result):
    if left_result[i]["start"] < right_result[j]["start"]:
        current_speaker_result = []
        while i < len(left_result) and left_result[i]["start"] < right_result[j]["start"]:
            current_speaker_result.append(left_result[i]["word"])
            i += 1
        merged_result.append(f"{speaker_mapping[current_speaker]}:{' '.join(current_speaker_result)}")
        current_speaker = "right"
    else:
        current_speaker_result = []
        while j < len(right_result) and right_result[j]["start"] < left_result[i]["start"]:
            current_speaker_result.append(right_result[j]["word"])
            j += 1
        merged_result.append(f"{speaker_mapping[current_speaker]}:{' '.join(current_speaker_result)}")
        current_speaker = "left"

# Обработка оставшихся результатов
while i < len(left_result):
    current_speaker_result = []
    while i < len(left_result):
        current_speaker_result.append(left_result[i]["word"])
        i += 1
    merged_result.append(f"{speaker_mapping[current_speaker]}:{' '.join(current_speaker_result)}")

while j < len(right_result):
    current_speaker_result = []
    while j < len(right_result):
        current_speaker_result.append(right_result[j]["word"])
        j += 1
    merged_result.append(f"{speaker_mapping[current_speaker]}:{' '.join(current_speaker_result)}")

# Создаем предложение из объединенных результатов
dialog = "\n".join(merged_result)

# Выводим текст диалога
print(dialog)

