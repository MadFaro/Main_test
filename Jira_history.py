import subprocess

# Входной и выходной файлы
input_file = 'input.mp3'
output_file = 'output.mp3'

# Команда FFmpeg для увеличения громкости в два раза
volume_command = ['ffmpeg', '-i', input_file, '-af', 'volume=2.0', output_file]
compand_command = ['ffmpeg', '-i', input_file, '-af', 'compand=0|0:1|1:-90/-900|-70/-70|-30/-9|0/-3:6:0:0:0', output_file]
# Запуск команды с помощью subprocess
subprocess.run(volume_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

print("Готово!")
