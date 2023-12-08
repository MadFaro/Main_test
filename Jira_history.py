
ffmpeg -i test.wav -filter:a loudnorm -ar 8000 -c:a pcm_s16le test2.wav
ffmpeg -i test.wav -filter:a loudnorm -ar 8000 -c:a pcm_s16le -b:a 128k -ac 2 test2.wav
ffmpeg -i test2.wav -af "volume=3.5" test3.wav
ffmpeg -i test3.wav -filter:a "atempo=0.95" test4.wav
ffmpeg -i input.wav -ar 16000 output.wav
ffmpeg -i output.wav -af "highpass=f=300, lowpass=f=3000" output1.wav
ffmpeg -i output1.wav -af "volume=1.5" output2.wav
ffmpeg -i output2.wav -af "equalizer=f=1000:width_type=h:w=200:g=5" output3.wav
ffmpeg -i output3.wav -af "crystalizer" output4.wav

Наличие слов запрещенных слов со стороны оператора
Наличие озвученного предложения/продажи ПК 
Наличие озвученного предложения/продажи КК 
Наличие отработки возражений в случае закрытия КК
Наличие отработки возражений в случае закрытия ДК
Наличие отработки возражений в случае отключения услуги "Моя защита"
Наличие отработки возражений в случае снижения Лимита по КК
Наличие кросс-продажи второго продукта
Основные причина не получения продукта на FU
Использование механик и причины закрытия карты Retention
Основные причины отказов на разных кампаниях
