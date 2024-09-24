import win32com.client, time, datetime, win32gui, win32ui, os
from ctypes import windll
from PIL import Image
import pandas as pd

end = datetime.datetime.strptime('18:30:00', '%H:%M:%S').time()
start = datetime.datetime.strptime('09:00:00', '%H:%M:%S').time()

names = {'Windows Script Host', 'Файл уже используется', 'Microsoft Excel', 'Безопасность Windows'}

hndle = []

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
			with open(str(name) + '.png', "rb") as file:
				#bots.sendDocument(chat_id='697716958', document=file, caption = str(name))
				file.close
			os.remove(str(name) + '.png')

	if now < datetime.datetime.strptime('00:15:00', '%H:%M:%S').time() and now > datetime.datetime.strptime('00:00:00', '%H:%M:%S').time():
		hndle.clear()
	time.sleep(60)
