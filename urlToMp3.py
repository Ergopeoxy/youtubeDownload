# importing packages
from pytube import YouTube, Playlist
import os


def downloadMp3(yt, askPath=0):
    # extract only audio
    video = yt.streams.filter(only_audio=True).first()

    destination = '.'
    # check for destination to save file
    if(askPath==1):
        print("Enter the destination (leave blank for current directory)")
        destination = str(input(">> ")) or '.'

    # download the file
    out_file = video.download(output_path=destination)

    # save the file
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)

# url input from user
def single():
    yt = YouTube(str(input("Enter the URL of the video you want to download: \n>> ")))
    downloadMp3(yt,1)
   
playlistFlag = str(input("playlist or single vid? 1=playlist 0-single (defualt 0) \n>> ")) or '0'





def playlist():
    p = Playlist(str(input("Enter the URL of the video you want to download: \n>> ")))
    for video in p.videos:
       downloadMp3(video)

if playlistFlag=='0':
    single()
else:
    playlist()

