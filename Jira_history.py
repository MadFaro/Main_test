
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

import os, time, datetime
import win32com.client

Yesterday1 = (datetime.date.today() - datetime.timedelta(days=1)).strftime('%d')
Yesterday2 = (datetime.date.today() - datetime.timedelta(days=1)).strftime('%m')
Yesterday3 = (datetime.date.today() - datetime.timedelta(days=1)).strftime('%Y')

months = ["День", "Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"]
month = (months[int(Yesterday2)])

file = "\\\\Fs-vrn-cp002\\claim\\Отчетность сервисных групп\\Отчеты групп\\ГПСО\\Отчет по ПП\\Эффективность claim "+month+" "+Yesterday3+" по столбцу Исполнитель ОК.xlsx"
file1 = "\\\\Fs-vrn-cp002\\claim\\Отчетность сервисных групп\\Отчеты групп\\Общие отчеты\\ТД\\"+Yesterday3+"\\"+month+" "+Yesterday3+"\\Пропущенные звонки "+month+".xlsx"
file2= "\\\\Fs-vrn-cp002\\claim\\Отчетность сервисных групп\\Отчеты групп\\Общие отчеты\\ТД\\"+Yesterday3+"\\"+month+" "+Yesterday3+"\\ГПСО обеды перерывы "+month+".xlsx"
file3 = "\\\\Fs-vrn-cp002\\claim\\Отчетность сервисных групп\\Отчеты групп\\Сервисы\\Отчет по SMS\\Отчет по отправленным SMS\\"+Yesterday3+"\\Отправленные "+month+".xlsx"
file4 = "\\\\Fs-vrn-cp002\\claim\\Отчетность сервисных групп\\Отчеты групп\\Общие отчеты\\ТД\\"+Yesterday3+"\\"+month+" "+Yesterday3+"\\Опоздания "+month+".xlsx"
file5 = "\\\\Fs-vrn-cp002\\claim\\Отчетность сервисных групп\\Отчеты групп\\Общие отчеты\\FCR\\FCR EOO\\Регистрация в ЕОО_"+month+" "+Yesterday3+" + % регистрации.xlsx"
file6 = "\\\\Fs-vrn-cp002\\claim\\Отчетность сервисных групп\\Отчеты групп\\Общие отчеты\\FCR\\FCR EOO\\% регистрации " + Yesterday3 + ".xlsx"
file7 = "\\\\Fs-vrn-cp002\\claim\\Отчетность сервисных групп\\Отчеты групп\\Общие отчеты\\FCR\\FCR EOO\\NPS повторы ЦОВ.xlsm"
file8 = "\\\\Fs-vrn-cp002\\claim\\Отчетность сервисных групп\\Отчеты групп\\ГПСО\\Запросы в NPS\\ССО.xlsx"
file9 = "\\\\Fs-vrn-cp002\\claim\\Отчетность сервисных групп\\Отчеты групп\\ГПСО\\Отчет по ACW\\СО ACW.xlsx"

HTMLBody = ("Добрый день!<BR> <style type= text/css >"
            "A{color: #f00}"
            "table {border-collapse: collapse; background: #333;border: 1px solid #333;text-align: center;}"
            "table th {font-size: 15px;padding: 10px;text-align: center;color:#ffffff;border: 1px solid #333}" 
            "table td {background: #f0f0f0;padding: 10px;text-align: left;border: 1px solid #333}"
			"</style> <table border: 1px solid #000 class= brd > <tr> <th>Отчет</th> <th>Дата и время<BR>обновления</th></tr>"
			"<tr> <td> <a href ="+'"'+ file + '"'+">" + os.path.basename(file) + "</A> </td> <td>" + str(datetime.datetime.strptime(time.ctime(os.path.getmtime(file)), "%c").strftime('%d.%m.%Y - %H:%M:%S')) + "</td> "
			"<tr> <td> <a href = "+'"'+ file1 + '"'+">" + os.path.basename(file1) + "</A> </td> <td>" + str(datetime.datetime.strptime(time.ctime(os.path.getmtime(file1)), "%c").strftime('%d.%m.%Y - %H:%M:%S')) + "</td> "
			"<tr> <td> <a href = "+'"'+ file2 + '"'+">" + os.path.basename(file2) + "</A> </td> <td>" + str(datetime.datetime.strptime(time.ctime(os.path.getmtime(file2)), "%c").strftime('%d.%m.%Y - %H:%M:%S')) + "</td> "
			"<tr> <td> <a href = "+'"'+ file3 + '"'+">" + os.path.basename(file3) + "</A> </td> <td>" + str(datetime.datetime.strptime(time.ctime(os.path.getmtime(file3)), "%c").strftime('%d.%m.%Y - %H:%M:%S')) + "</td> "
			"<tr> <td> <a href = "+'"'+ file4 + '"'+">" + os.path.basename(file4) + "</A> </td> <td>" + str(datetime.datetime.strptime(time.ctime(os.path.getmtime(file4)), "%c").strftime('%d.%m.%Y - %H:%M:%S')) + "</td> "
			"<tr> <td> <a href = "+'"'+ file5 + '"'+">" + os.path.basename(file5) + "</A> </td> <td>" + str(datetime.datetime.strptime(time.ctime(os.path.getmtime(file5)), "%c").strftime('%d.%m.%Y - %H:%M:%S')) + "</td> "
			"<tr> <td> <a href = "+'"'+ file6 + '"'+">" + os.path.basename(file6) + "</A> </td> <td>" + str(datetime.datetime.strptime(time.ctime(os.path.getmtime(file6)), "%c").strftime('%d.%m.%Y - %H:%M:%S')) + "</td> "
			"<tr> <td> <a href = "+'"'+ file7 + '"'+">" + os.path.basename(file7) + "</A> </td> <td>" + str(datetime.datetime.strptime(time.ctime(os.path.getmtime(file7)), "%c").strftime('%d.%m.%Y - %H:%M:%S')) + "</td> "
			"<tr> <td> <a href = "+'"'+ file8 + '"'+">" + os.path.basename(file8) + "</A> </td> <td>" + str(datetime.datetime.strptime(time.ctime(os.path.getmtime(file8)), "%c").strftime('%d.%m.%Y - %H:%M:%S')) + "</td> "
			"<tr> <td> <a href = "+'"'+ file9 + '"'+">" + os.path.basename(file9) + "</A> </td> <td>" + str(datetime.datetime.strptime(time.ctime(os.path.getmtime(file9)), "%c").strftime('%d.%m.%Y - %H:%M:%S')) + "</td> ")

outlook = win32com.client.Dispatch( "Outlook.Application" )
mail = outlook.CreateItem(0)
#mail.To = "atologonov@svyaznoy.ru"
mail.To = "kbelyaeva@svyaznoy.ru"
mail.Subject = 'Отчеты ГПСО '
mail.HTMLBody = HTMLBody

mail.Send()


