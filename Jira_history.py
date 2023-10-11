
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


Option Explicit

Dim objExcel, objWorkbook

' Создаем объект Excel
Set objExcel = CreateObject("Excel.Application")

' Открываем файл Excel
Set objWorkbook = objExcel.Workbooks.Open("путь_к_вашему_файлу\запрос1.xlsx")

' Замените "Имя_подключения" на имя вашего подключения данных
Dim connectionName
connectionName = "Имя_подключения"

' Обновляем конкретное подключение данных
On Error Resume Next
objWorkbook.Connections(connectionName).Refresh
On Error GoTo 0

' Сохраняем и закрываем файл Excel
objWorkbook.Save
objWorkbook.Close

' Высвобождаем ресурсы
Set objWorkbook = Nothing
Set objExcel = Nothing

