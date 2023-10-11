
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


set App = createobject("excel.application")
App.visible = false
App.Workbooks.Open("C:\Users\atologonov\Desktop\ÃÎÏ\OR\ORMail.xlsm")
App.Run("ORMail.xlsm!Pochta")
App.Workbooks("ORMail.xlsm").Close(false)
App.quit


Sub ORZ()
Calculate

Dim book1, book2, n1, n2 As String

book1 = Worksheets("Data").Range("A1")
book2 = Worksheets("Data").Range("A2")

n1 = Dir(book1)
n2 = Dir(book2)

Workbooks.Open (book1), False, False, , , 255
Workbooks(n1).Connections("Çàïðîñ èç Portals").Refresh
Calculate
Workbooks(n1).RefreshAll
Workbooks(n1).Save
Workbooks(n1).Close

Workbooks.Open (book2), False, False, , , 255
Workbooks(n2).Connections("Çàïðîñ èç Portals").Refresh
Calculate
Workbooks(n2).RefreshAll
Workbooks(n2).Save
Workbooks(n2).Close

End Sub
