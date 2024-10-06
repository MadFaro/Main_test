os.system('taskkill /F /IM OUTLOOK.EXE')
outlook_path = r"C:\Program Files\Microsoft Office\root\Office16\OUTLOOK.EXE"
subprocess.Popen(outlook_path)
