
ffmpeg -i test.wav -filter:a loudnorm -ar 8000 -c:a pcm_s16le test2.wav
ffmpeg -i test.wav -filter:a loudnorm -ar 8000 -c:a pcm_s16le -b:a 128k -ac 2 test2.wav
ffmpeg -i test2.wav -af "volume=3.5" test3.wav
ffmpeg -i test3.wav -filter:a "atempo=0.95" test4.wav


ffmpeg -i input.wav -ar 16000 output.wav
ffmpeg -i output.wav -af "highpass=f=300, lowpass=f=3000" output1.wav
ffmpeg -i output1.wav -af "volume=1.5" output2.wav
ffmpeg -i output2.wav -af "equalizer=f=1000:width_type=h:w=200:g=5" output3.wav
ffmpeg -i output3.wav -af "crystalizer" output4.wav
=ЕСЛИОШИБКА((((@Agents($AH$2;$AI$2;I18;I68)/30)*22,5)/0,85)/I166;2)


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from bs4 import BeautifulSoup as BS

def browser_chrome():
    options = Options()
    #options.add_argument('headless')
    options.add_argument('window-size=1920x935')
    driver = webdriver.Chrome(executable_path=r'C:\путь\chromedriver.exe', options=options)
    driver.get('https://vstup.osvita.ua/y2021/r14/97/833553')
    driver.execute_script('getItemsRequest()') # Нажимает кнопку
    time.sleep(5)
    body = driver.execute_script('return document.getElementsByTagName("body")[0]') 
    html_page = body.get_attribute('innerHTML')
    html = BS(html_page, 'html.parser')
    trs = html.select('.rstatus6')
    for el in trs:
        t = el.find_all('td')
        print(f'{t[0].text}|{t[1].text}|{t[2].text}')

browser_chrome()

