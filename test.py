import win32com.client as win32

# Создание экземпляра приложения Outlook
outlook = win32.Dispatch('outlook.application')

# Создание нового письма
mail = outlook.CreateItem(0)

# Настройка получателей, темы и тела письма
mail.To = 'recipient@example.com'  # получатель
mail.Subject = 'Письмо с изображением в теле'
mail.HTMLBody = '''
<html>
<body>
    <h2>Привет!</h2>
    <p>Вот изображение, встроенное в тело письма:</p>
    <img src="cid:MyImage">
</body>
</html>
'''

# Путь к картинке, которую нужно вставить в тело письма
image_path = r'C:\path\to\your\image.jpg'

# Добавление картинки как вложения и установка Content-ID
attachment = mail.Attachments.Add(image_path)
attachment.PropertyAccessor.SetProperty("http://schemas.microsoft.com/mapi/proptag/0x3712001F", "MyImage")

# Отправка письма (раскомментируй для отправки)
# mail.Send()

# Открыть письмо для предварительного просмотра перед отправкой
mail.Display(True)

