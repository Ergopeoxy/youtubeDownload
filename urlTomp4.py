# importing packages
from pytube import YouTube, Playlist
import os


def downloadMp3(yt, askPath=0):
  
    video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    destination = 'mp4File'
    # check for destination to save file
    if(askPath==1):
        print("Enter the destination (leave blank for default dir mp4File)")
        destination = str(input(">> ")) or 'mp4File'

    # download the file
    out_file = video.download(output_path=destination)

    # save the file
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp4'
    os.rename(out_file, new_file)
    # result of success
    print(yt.title + " has been successfully downloaded.")


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

