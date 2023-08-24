ffmpeg -i test.wav -filter:a loudnorm -ar 8000 test2.wav
ffmpeg -i test2.wav -af "volume=3.5" test3.wav
