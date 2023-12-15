
ffmpeg -i test.wav -filter:a loudnorm -ar 8000 -c:a pcm_s16le test2.wav
ffmpeg -i test.wav -filter:a loudnorm -ar 8000 -c:a pcm_s16le -b:a 128k -ac 2 test2.wav
ffmpeg -i test2.wav -af "volume=3.5" test3.wav
ffmpeg -i test3.wav -filter:a "atempo=0.95" test4.wav
ffmpeg -i input.wav -ar 16000 output.wav
ffmpeg -i output.wav -af "highpass=f=300, lowpass=f=3000" output1.wav
ffmpeg -i output1.wav -af "volume=1.5" output2.wav
ffmpeg -i output2.wav -af "equalizer=f=1000:width_type=h:w=200:g=5" output3.wav
ffmpeg -i output3.wav -af "crystalizer" output4.wav


import requests
import json

REPORT_HOST = 'https://url_api'
TOKEN = 'ваш_токен'
USER_NAME = 'ваше_имя'

def headers():
    return {
        'Accept': 'application/json',
        'Content-type': 'application/json',
        'Authorization': f'Token token={TOKEN}, user_name={USER_NAME}'
    }

def make_post(url, params):
    response = requests.post(url, json=params, headers=headers())
    response.raise_for_status()

    return response.status_code, response.json()

# В виде файла:
res_status, res_body = make_post(f'{REPORT_HOST}/api/reports/22', {
    'format': 'file',
    'params': {
        'd1': '01.01.2021',
        'd2': '01.02.2021'
    }
})

if res_body:
    with open('file1.xlsx', 'wb') as file:
        file.write(res_body)
