ffmpeg -i test.wav -af "equalizer=f=3000:width_type=h:width=200:g=5" test2.wav
ffmpeg -i test.wav -af "highpass=f=100,highshelf=f=1000:width_type=o:w=200:g=5" test2.wav
ffmpeg -i test.wav -af "dynaudnorm" test2.wav
ffmpeg -i test.wav -af "acompressor" test2.wav
