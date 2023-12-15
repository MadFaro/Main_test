
ffmpeg -i test.wav -filter:a loudnorm -ar 8000 -c:a pcm_s16le test2.wav
ffmpeg -i test.wav -filter:a loudnorm -ar 8000 -c:a pcm_s16le -b:a 128k -ac 2 test2.wav
ffmpeg -i test2.wav -af "volume=3.5" test3.wav
ffmpeg -i test3.wav -filter:a "atempo=0.95" test4.wav
ffmpeg -i input.wav -ar 16000 output.wav
ffmpeg -i output.wav -af "highpass=f=300, lowpass=f=3000" output1.wav
ffmpeg -i output1.wav -af "volume=1.5" output2.wav
ffmpeg -i output2.wav -af "equalizer=f=1000:width_type=h:w=200:g=5" output3.wav
ffmpeg -i output3.wav -af "crystalizer" output4.wav

#encoding: utf-8
require 'httpclient'
require 'json'

REPORT_HOST = 'https://url_api'
TOKEN = 'ваш_токен'
USER_NAME = 'ваше_имя'

def headers
  {
    'Accept' => 'application/json',
    'Content-type' => 'application/json',
    'Authorization' => " Token token=#{TOKEN}, user_name=#{USER_NAME}"
  }
end

def make_post(url, params)
  uri = URI(url)
  clnt = HTTPClient.new
  res = clnt.post(uri, params.to_json, headers)
  body = JSON.load(res.content)
  [res.status, body]
rescue => err
  [500, err.message]
end

# В виде файла:
res = make_post("#{REPORT_HOST}/api/reports/22", {
  'format' => 'file',
  'params' => {
    'd1' => '01.01.2021',
    'd2' => '01.02.2021'
  }
})
unless res.blank?
  f = File.new(Rails.root.join('tmp', 'file1.xlsx'), "wb")
  f.write(res)
  f.close
end
