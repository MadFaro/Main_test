ffmpeg -i input_audio.mp3 -f segment -segment_time 30 -c copy output_segments/segment_%03d.mp3
