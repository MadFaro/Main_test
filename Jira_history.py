ffmpeg -i test.wav -filter:a loudnorm -ar 16000 -c:a pcm_s16le -b:a 256k test2.wav
ffmpeg -i test2.wav -af "volume=1.2" test3.wav
