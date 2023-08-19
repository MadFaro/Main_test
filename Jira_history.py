    adjusted_audio_l = audio_segment_l.speedup(playback_speed=speed_change)
  File "C:\Python38\lib\site-packages\pydub\effects.py", line 91, in speedup
    out = out.append(chunk, crossfade=crossfade)
  File "C:\Python38\lib\site-packages\pydub\audio_segment.py", line 1264, in append
    xf = seg1[-crossfade:].fade(to_gain=-120, start=0, end=float('inf'))
  File "C:\Python38\lib\site-packages\pydub\audio_segment.py", line 1362, in fade
    sample = audioop.mul(sample, self.sample_width, volume_change)
audioop.error: Size should be 1, 2, 3 or 4
