
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

import openpyxl

# Откройте исходную книгу
source_wb = openpyxl.load_workbook('your_source_file.xlsx')

# Создайте новую книгу
new_wb = openpyxl.Workbook()

# Выберите листы для копирования
sheet_names_to_copy = ['Sheet1', 'Sheet2']  # Замените на имена листов, которые вы хотите скопировать

# Копируйте листы в новую книгу
for sheet_name in sheet_names_to_copy:
    source_sheet = source_wb[sheet_name]
    new_sheet = new_wb.create_sheet(sheet_name)
    for row in source_sheet.iter_rows(values_only=True):
        new_sheet.append(row)

# Сохраните новую книгу
new_wb.save('new_combined_workbook.xlsx')
