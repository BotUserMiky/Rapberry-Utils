import numpy as np
import os
import matplotlib.pyplot as plt
import librosa
import wave
import slice

def setup():
    clear()
    slice.setup()
    t = open("output.txt", "x")
    t.close()
    try:
        os.mkdir("out")
    except:
        pass

def clear():
    slice.clear()
    os.remove("output.txt")
    try:
        while True:
            os.remove("out/Temp " + str(i) + ".png")
    except:
        return

setup()

print("setup done")

audio = "audio.wav"

count = slice.slice(audio,0.014)
#slice.slice(audio, 10)
print("done slicing")

with open("output.txt", "a") as file:
    try:
        i = 0
        while True:
            audio_path = "temp_audio/temp_" + str(i) + ".wav" 
            audio, sr = librosa.load(audio_path)

            audio_ft = np.fft.fft(audio)

            magnitude = np.abs(audio_ft)

            #plt.figure(figsize=(18,5))

            freq = np.linspace(0, sr, len(magnitude))

            bins = int(len(freq) * 0.5)

            highest_index = np.argmax(magnitude[:bins])

            #plt.plot(freq[:bins], magnitude[:bins])
            #plt.xlabel("Frequencies")
            #plt.title("Temp " + str(i))

            #plt.savefig("out/Temp " + str(i))

            #plt.close()
            print("Fourrier transform done for: " + ''.join(str(int((i/count)*100))) + "% of all files     ", end="\r")
            file.write(str(freq[highest_index]) + "," + str(slice.get_length(audio_path)) + ":\n")
            i += 1
    except:
        pass

slice.clear()