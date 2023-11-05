
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

merged_output = []
i, j = 0, 0

while i < len(output1) and j < len(output2):
    word1 = output1[i]
    word2 = output2[j]

    if word1["start"] < word2["start"]:
        merged_output.append(word1)
        i += 1
    else:
        merged_output.append(word2)
        j += 1

# Add any remaining words from both outputs
merged_output.extend(output1[i:])
merged_output.extend(output2[j:])

# Create a sentence from the merged output
sentence = " ".join(word["word"] for word in merged_output)

print(sentence)

