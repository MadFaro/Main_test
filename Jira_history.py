
ffmpeg -i test.wav -filter:a loudnorm -ar 8000 -c:a pcm_s16le test2.wav
ffmpeg -i test.wav -filter:a loudnorm -ar 8000 -c:a pcm_s16le -b:a 128k -ac 2 test2.wav
ffmpeg -i test2.wav -af "volume=3.5" test3.wav
ffmpeg -i test3.wav -filter:a "atempo=0.95" test4.wav
ffmpeg -i input.wav -ar 16000 output.wav
ffmpeg -i output.wav -af "highpass=f=300, lowpass=f=3000" output1.wav
ffmpeg -i output1.wav -af "volume=1.5" output2.wav
ffmpeg -i output2.wav -af "equalizer=f=1000:width_type=h:w=200:g=5" output3.wav
ffmpeg -i output3.wav -af "crystalizer" output4.wav

select *
from table ch
where ch.DESCRIPTION = 'Перевести клиента на группу удержания при запросе клиента на закрытие карты'
and ch.CAMPAIGN_NAME = 'RETENTION_5589'
and ch.CHANNEL = 'RETENTION'
and contact_dt>sysdate-90
and IS_CONTROL_CELL=1
and (CONTACT_STATUS_NAME in 'Control' and trunc(to_date('18.12.2023')) between CONTACT_DT and trunc(OFFER_EXPIRATION_DT)
     or CONTACT_STATUS_NAME in ('Stopped', 'Stopping') and trunc(to_date('18.12.2023')) between CONTACT_DT and trunc(CONTACT_DATE_TIME))
