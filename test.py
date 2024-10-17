import win32com.client
import time
import datetime
import os

# Подключение к Outlook
outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")

# Получение папки
folder_sl = outlook.GetSharedDefaultFolder(outlook.CreateRecipient("atologonov@svyaznoy.ru"), 6).Folders['УС']

# Папка для сохранения вложений
attachment_folder = "C:\\path\\to\\save\\attachments"  # Укажите путь к папке

# Функция для сохранения вложений
def save_attachments(message):
    if message.Attachments.Count > 0:
        for attachment in message.Attachments:
            attachment.SaveAsFile(os.path.join(attachment_folder, attachment.FileName))
            print(f"Вложение {attachment.FileName} сохранено.")

# Бесконечный цикл для проверки новых писем
while True:
    today = datetime.date.today()  # Получаем текущую дату
    
    # Проходим по всем письмам в папке
    for mess in folder_sl.Items:
        # Если письмо было отправлено сегодня
        if mess.senton.date() == today:
            save_attachments(mess)  # Сохраняем вложения
            
    time.sleep(60)  # Проверка каждые 60 секунд

