ffmpeg -i test.wav -filter:a loudnorm -ar 16000 -c:a pcm_s16le -b:a 256k test.wav

