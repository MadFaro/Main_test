
ffmpeg -i test.wav -filter:a loudnorm -ar 8000 -c:a pcm_s16le test2.wav
ffmpeg -i test.wav -filter:a loudnorm -ar 8000 -c:a pcm_s16le -b:a 128k -ac 2 test2.wav
ffmpeg -i test2.wav -af "volume=3.5" test3.wav
ffmpeg -i test3.wav -filter:a "atempo=0.95" test4.wav
ffmpeg -i input.wav -ar 16000 output.wav
ffmpeg -i output.wav -af "highpass=f=300, lowpass=f=3000" output1.wav
ffmpeg -i output1.wav -af "volume=1.5" output2.wav
ffmpeg -i output2.wav -af "equalizer=f=1000:width_type=h:w=200:g=5" output3.wav
ffmpeg -i output3.wav -af "crystalizer" output4.wav

    nlp_ru = spacy.load("ru_core_news_sm")
  File "C:\Python38\lib\site-packages\spacy\__init__.py", line 47, in load
    return util.load_model(name, disable=disable, exclude=exclude, config=config)
  File "C:\Python38\lib\site-packages\spacy\util.py", line 329, in load_model
    raise IOError(Errors.E050.format(name=name))
OSError: [E050] Can't find model 'ru_core_news_sm'. It doesn't seem to be a Python package or a valid path to a data directory.
