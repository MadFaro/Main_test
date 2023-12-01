
ffmpeg -i test.wav -filter:a loudnorm -ar 8000 -c:a pcm_s16le test2.wav
ffmpeg -i test.wav -filter:a loudnorm -ar 8000 -c:a pcm_s16le -b:a 128k -ac 2 test2.wav
ffmpeg -i test2.wav -af "volume=3.5" test3.wav
ffmpeg -i test3.wav -filter:a "atempo=0.95" test4.wav
ffmpeg -i input.wav -ar 16000 output.wav
ffmpeg -i output.wav -af "highpass=f=300, lowpass=f=3000" output1.wav
ffmpeg -i output1.wav -af "volume=1.5" output2.wav
ffmpeg -i output2.wav -af "equalizer=f=1000:width_type=h:w=200:g=5" output3.wav
ffmpeg -i output3.wav -af "crystalizer" output4.wav


Args:
  model_size_or_path: Size of the model to use (tiny, tiny.en, base, base.en,
    small, small.en, medium, medium.en, large-v1, large-v2, or large), a path to a converted model directory, or a CTranslate2-converted Whisper model ID from the Hugging Face Hub. When a size or a model ID is configured, the converted model is downloaded from the Hugging Face Hub.
  device: Device to use for computation ("cpu", "cuda", "auto").
  device_index: Device ID to use.
    The model can also be loaded on multiple GPUs by passing a list of IDs (e.g. [0, 1, 2, 3]). In that case, multiple transcriptions can run in parallel when transcribe() is called from multiple Python threads (see also num_workers).
  compute_type: Type to use for computation.
    See https://opennmt.net/CTranslate2/quantization.html.
  cpu_threads: Number of threads to use when running on CPU (4 by default).
    A non zero value overrides the OMP_NUM_THREADS environment variable.
  num_workers: When transcribe() is called from multiple Python threads,
    having multiple workers enables true parallelism when running the model (concurrent calls to self.model.generate() will run in parallel). This can improve the global throughput at the cost of increased memory usage.
  download_root: Directory where the models should be saved. If not set, the models
    are saved in the standard Hugging Face cache directory.
  local_files_only: If True, avoid downloading the file and return the path to the
    local cached file if it exists.
