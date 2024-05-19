import wave
import contextlib
import os

def slice(file_name, time):
    data, framerate, sample_width, channels = read(file_name)
    max = (int(int(get_length(file_name))//time))+1
    coefficients = int(sample_width*time*framerate*channels)
    for i in range(max):
        with open("temp_audio/temp_" + str(i) + ".wav", "x") as file:
            pass
        with wave.open("temp_audio/temp_" + str(i) + ".wav", "w") as outfile:
            outfile.setnchannels(channels)
            outfile.setsampwidth(sample_width)
            outfile.setframerate(framerate)
            outfile.setnframes(int(int(len(data) / sample_width)//time))
            start = i*coefficients
            if i != max-1:
                outfile.writeframes(data[start:start+coefficients])
            else:
                outfile.writeframes(data[start:])
    return max
    

def read(file_name):
    with wave.open(file_name, "rb") as file:
        channels = file.getnchannels()
        sample_width = file.getsampwidth()
        framerate = file.getframerate()
        duration = get_length(file_name)
        data = file.readframes(int((duration) * framerate))
        return data, framerate, sample_width, channels

def get_length(file_name):
    with contextlib.closing(wave.open(file_name,'r')) as f:
        frames = f.getnframes()
        rate = f.getframerate()
        duration = frames / float(rate)
        return duration

def clear():
    i = 0
    try:
        while True:
            os.remove("temp_audio/temp_" + str(i) + ".wav")
            i+=1
    except:
        return

def setup():
    try:
        os.mkdir("temp_audio")
    except:
        pass

if __name__ == "__main__":
    print(get_length("audio.wav"))
    clear()
    slice("audio.wav", 0.014)