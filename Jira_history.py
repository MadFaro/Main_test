from pydub import AudioSegment
from pydub.playback import play

input_audio = AudioSegment.from_file("input_audio.mp3")
segment_length = 30 * 1000  # 30 секунд в миллисекундах

segments = []

i = 0
while i < len(input_audio):
    segment = input_audio[i:i+segment_length]

    # Найдем индекс паузы в текущем сегменте
    pause_idx = segment.rfind_b(" ")  # Поиск последнего пробела

    if pause_idx != -1:
        # Обрежем сегмент до индекса паузы
        segment = segment[:pause_idx+1]

    segments.append(segment)
    i += len(segment)

# Сохраняем сегменты
for idx, segment in enumerate(segments):
    output_path = f"output_segments/segment_{idx:03d}.mp3"
    segment.export(output_path, format="mp3")

print("Сегментация завершена.")
