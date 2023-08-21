ffmpeg -i input_audio.mp3 -f segment -segment_time 30 -c copy output_segments/segment_%03d.mp3

texts = []

bw_ext_audio, sr = librosa.load(bw_file, sr = 16_000)

current_prompt = None
current_prefix = None

for i, r in df.iterrows():
    
    bw_ext_segment = bw_ext_audio[int(r["start"]*sr) : int(r["end"]*sr)]
    #results = model.transcribe(bw_ext_segment, language = "it")
    results = model.transcribe(bw_ext_segment, 
                               language = "it", 
                               prompt = current_prompt,
                               prefix = current_prefix,
                               condition_on_previous_text = True)
    
    text = results["text"]
    
    current_prompt = text
    current_prefix = text

    texts.append(text)

df["text"] = texts

import torch
from transformers import pipeline
from datasets import load_dataset

device = "cuda:0" if torch.cuda.is_available() else "cpu"

pipe = pipeline(
  "automatic-speech-recognition",
  model="openai/whisper-large-v2",
  chunk_length_s=30,
  device=device,
)

ds = load_dataset("hf-internal-testing/librispeech_asr_dummy", "clean", split="validation")
sample = ds[0]["audio"]

prediction = pipe(sample.copy(), batch_size=8)["text"]

# we can also return timestamps for the predictions
prediction = pipe(sample.copy(), batch_size=8, return_timestamps=True)["chunks"]
