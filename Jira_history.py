ffmpeg -i input.wav -af "aselect='gte(duration,2)', asetpts=N/SR/TB" -f segment -segment_time 2 output%d.wav
