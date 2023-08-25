ffmpeg -i test.wav -filter:a loudnorm -ar 8000 -c:a pcm_s16le test2.wav
ffmpeg -i test.wav -filter:a loudnorm -ar 8000 -c:a pcm_s16le -b:a 128k -ac 2 test2.wav
ffmpeg -i test2.wav -af "volume=3.5" test3.wav
ffmpeg -i test3.wav -filter:a "atempo=0.95" test4.wav
ОКРУГЛВВЕРХ(ЕСЛИ(E$1>$A2;(E$1*($B2*$A2+$B2*(1-$A2))-$B2*$A2)/(1-E$1);(-1)*(($B2*$A2)-E$1*($B2*$A2+$B2*(1-$A2)))/E$1);0)
