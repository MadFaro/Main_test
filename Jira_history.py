import soundfile as sf
 
audio_data, sample_rate = sf.read(file)
left_channel = audio_data[:, 0]
right_channel = audio_data[:, 1]

max_value_l = np.max(np.abs(left_channel))
if max_value_l > 0:
 normalize_audio_l = left_channel / max_value_l
else:
 normalize_audio_l = left_channel

max_value_r = np.max(np.abs(right_channel))
 if max_value_r > 0:
normalize_audio_r = right_channel / max_value_r
else:
 normalize_audio_r = right_channel
