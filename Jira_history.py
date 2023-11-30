
ffmpeg -i test.wav -filter:a loudnorm -ar 8000 -c:a pcm_s16le test2.wav
ffmpeg -i test.wav -filter:a loudnorm -ar 8000 -c:a pcm_s16le -b:a 128k -ac 2 test2.wav
ffmpeg -i test2.wav -af "volume=3.5" test3.wav
ffmpeg -i test3.wav -filter:a "atempo=0.95" test4.wav
ffmpeg -i input.wav -ar 16000 output.wav
ffmpeg -i output.wav -af "highpass=f=300, lowpass=f=3000" output1.wav
ffmpeg -i output1.wav -af "volume=1.5" output2.wav
ffmpeg -i output2.wav -af "equalizer=f=1000:width_type=h:w=200:g=5" output3.wav
ffmpeg -i output3.wav -af "crystalizer" output4.wav

from transformers import Wav2Vec2ForCTC, Wav2Vec2Tokenizer
import torchaudio
import torch

# Загрузка предварительно обученной модели и токенизатора
model = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-base-960h")
tokenizer = Wav2Vec2Tokenizer.from_pretrained("facebook/wav2vec2-base-960h")

# Загрузка аудиофайла
audio_input, _ = torchaudio.load("your_audio_file.wav", normalize=True)

# Преобразование аудио в токены
input_values = tokenizer(audio_input.squeeze().numpy(), return_tensors="pt").input_values

# Распознавание аудио
with torch.no_grad():
    logits = model(input_values).logits

# Получение текста из выходных данных
predicted_ids = torch.argmax(logits, dim=-1)
transcription = tokenizer.batch_decode(predicted_ids)[0]

print("Transcription:", transcription)
