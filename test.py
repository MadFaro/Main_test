while 1 == 1:
    now = datetime.datetime.now().time()
    today = datetime.date.today()
    for name in names:
        if win32gui.FindWindow(None, name) != 0 and win32gui.FindWindow(None, name) not in hndle:
            hndle.append(win32gui.FindWindow(None, name))
            hwnd = win32gui.FindWindow(None, name)
            left, top, right, bot = win32gui.GetWindowRect(hwnd)
            w = right - left
            h = bot - top
            hwndDC = win32gui.GetWindowDC(hwnd)
            mfcDC  = win32ui.CreateDCFromHandle(hwndDC)
            saveDC = mfcDC.CreateCompatibleDC()
            saveBitMap = win32ui.CreateBitmap()
            saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)
            saveDC.SelectObject(saveBitMap)
            result = windll.user32.PrintWindow(hwnd, saveDC.GetSafeHdc(), 0)
            bmpinfo = saveBitMap.GetInfo()
            bmpstr = saveBitMap.GetBitmapBits(True)
            im = Image.frombuffer(
                                'RGB',
                                (bmpinfo['bmWidth'], bmpinfo['bmHeight']),
                                bmpstr, 'raw', 'BGRX', 0, 1)

            win32gui.DeleteObject(saveBitMap.GetHandle())
            saveDC.DeleteDC()
            mfcDC.DeleteDC()
            win32gui.ReleaseDC(hwnd, hwndDC)
            im.save(str(name) + '.png')
            time.sleep(10)
            try:
                try:
                    form_mail = format_tasks_for_email(get_running_tasks_from_root())
                except:
                    form_mail = ""
        
                mail = outlook.CreateItem(0)
                mail.To = 'TologonovAB@uralsib.ru'
                mail.Subject = 'Ошибка на ПК 7808'
                mail.HTMLBody = '''
                                                <html>
                                                <body>
                                                    <p>Ошибка:</p>
                                                    <img src="cid:MyImage">
                                                </body>
                                                </html>
                                                ''' + '<br><br>Список запущенных задач на данный момент:<br>' + form_mail
                attachment = mail.Attachments.Add('C:\\Users\\TologonovAB\\Desktop\\monitoring\\' + str(name) + '.png')
                attachment.PropertyAccessor.SetProperty("http://schemas.microsoft.com/mapi/proptag/0x3712001F", "MyImage")
                mail.Send()
                os.remove(str(name) + '.png')
            except:
                os.system('taskkill /F /IM OUTLOOK.EXE')
                time.sleep(10)
                subprocess.Popen(r"C:\Program Files\Microsoft Office\Office16\OUTLOOK.EXE")
                time.sleep(20)

    if now < datetime.datetime.strptime('00:15:00', '%H:%M:%S').time() and now > datetime.datetime.strptime('00:00:00', '%H:%M:%S').time():
        hndle.clear()
    time.sleep(60)
