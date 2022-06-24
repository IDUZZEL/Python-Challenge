import os
import pytube as ytb
def mp3():
    audio = vdata.streams.get_audio_only()
    file = audio.download('audios')
    mp4, ext = os.path.splitext(file)
    mp3 = mp4 + '.mp3'
    os.rename(file, mp3)
def mp4():
    video = vdata.streams.get_by_itag(22)
    video.download('videos')

if __name__ == "__main__":
    type = input("choose between mp3/mp4 : ")
    list = open('list', 'r')
    links = list.readlines()
    for line in links:
        link = line.strip()
        vdata = ytb.YouTube(link)
        if type == "mp3":
            mp3()
        if type == "mp4":
            mp4()

