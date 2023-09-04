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

SUBSTR('Лимит по карте *1234 увеличен до 60000', INSTR('Лимит по карте *1234 увеличен до 60000', 'до ') + LENGTH('до ')) AS TextAfterDо

tes.py:3: DeprecationWarning: executable_path has been deprecated, please pass in a Service object
  driver = webdriver.Chrome('chromedriver.exe')
Traceback (most recent call last):
  File "tes.py", line 3, in <module>
    driver = webdriver.Chrome('chromedriver.exe')
  File "C:\Python38\lib\site-packages\selenium\webdriver\chrome\webdriver.py", line 84, in __init__
    super().__init__(
  File "C:\Python38\lib\site-packages\selenium\webdriver\chromium\webdriver.py", line 104, in __init__
    super().__init__(
  File "C:\Python38\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 286, in __init__
    self.start_session(capabilities, browser_profile)
  File "C:\Python38\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 378, in start_session
    response = self.execute(Command.NEW_SESSION, parameters)
  File "C:\Python38\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 440, in execute
    self.error_handler.check_response(response)
  File "C:\Python38\lib\site-packages\selenium\webdriver\remote\errorhandler.py", line 209, in check_response
    raise exception_class(value)
selenium.common.exceptions.WebDriverException: Message: <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN""http://www.w3.org/TR/html4/strict.dtd">
<HTML><HEAD><TITLE>Not Found</TITLE>
<META HTTP-EQUIV="Content-Type" Content="text/html; charset=us-ascii"></HEAD>
<BODY><h2>Not Found</h2>
<hr><p>HTTP Error 404. The requested resource is not found.</p>
</BODY></HTML>
