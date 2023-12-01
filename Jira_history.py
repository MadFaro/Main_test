
ffmpeg -i test.wav -filter:a loudnorm -ar 8000 -c:a pcm_s16le test2.wav
ffmpeg -i test.wav -filter:a loudnorm -ar 8000 -c:a pcm_s16le -b:a 128k -ac 2 test2.wav
ffmpeg -i test2.wav -af "volume=3.5" test3.wav
ffmpeg -i test3.wav -filter:a "atempo=0.95" test4.wav
ffmpeg -i input.wav -ar 16000 output.wav
ffmpeg -i output.wav -af "highpass=f=300, lowpass=f=3000" output1.wav
ffmpeg -i output1.wav -af "volume=1.5" output2.wav
ffmpeg -i output2.wav -af "equalizer=f=1000:width_type=h:w=200:g=5" output3.wav
ffmpeg -i output3.wav -af "crystalizer" output4.wav



from concurrent.futures import ProcessPoolExecutor

def main():
    folder1_path = r'C:\Users\TologonovAB\Desktop\model_wisper\move1'
    folder2_path = r'C:\Users\TologonovAB\Desktop\model_wisper\move2'
    model_path = r"C:\Users\TologonovAB\Desktop\model_wisper\whisper-int8-2"

    result_file1 = 'text1.csv'
    result_file2 = 'text2.csv'

    with ProcessPoolExecutor() as executor:
        executor.submit(process_files, folder1_path, model_path, result_file1)
        executor.submit(process_files, folder2_path, model_path, result_file2)

if __name__ == "__main__":
    main()

