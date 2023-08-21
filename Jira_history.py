ffmpeg -i input.wav -filter_complex "[0:a]asegment=duration=10:pause_threshold=-50dB:break_duration=2:reset_timestamps=1[out]" -map "[out]" output%d.wav
