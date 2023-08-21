from transformers import pipeline

# Инициализация пайплайна для автоматического распознавания речи
pipe = pipeline(
  "automatic-speech-recognition",
  model="openai/whisper-large-v2",
  chunk_length_s=30
)

# Путь к аудиофайлу
audio_path = "path_to_audio_file.wav"

# Выполнение распознавания речи с разбивкой на сегменты по 30 секунд
results = pipe(audio_path)

# Обработка результатов
for i, result in enumerate(results):
    transcript = result["alternatives"][0]["transcript"]
    print(f"Segment {i+1}: {transcript}")

