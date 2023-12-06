
ffmpeg -i test.wav -filter:a loudnorm -ar 8000 -c:a pcm_s16le test2.wav
ffmpeg -i test.wav -filter:a loudnorm -ar 8000 -c:a pcm_s16le -b:a 128k -ac 2 test2.wav
ffmpeg -i test2.wav -af "volume=3.5" test3.wav
ffmpeg -i test3.wav -filter:a "atempo=0.95" test4.wav
ffmpeg -i input.wav -ar 16000 output.wav
ffmpeg -i output.wav -af "highpass=f=300, lowpass=f=3000" output1.wav
ffmpeg -i output1.wav -af "volume=1.5" output2.wav
ffmpeg -i output2.wav -af "equalizer=f=1000:width_type=h:w=200:g=5" output3.wav
ffmpeg -i output3.wav -af "crystalizer" output4.wav
import pandas as pd

16	02.11.23 00:00:00
16	02.11.23 00:54:34
16	02.11.23 01:00:07
16	02.11.23 01:09:48
16	02.11.23 03:17:07
16	02.11.23 03:31:15
16	02.11.23 03:53:07
16	02.11.23 03:59:24
16	02.11.23 04:09:13
16	02.11.23 04:52:17
16	02.11.23 04:59:18
16	02.11.23 04:59:26
16	02.11.23 17:00:21


