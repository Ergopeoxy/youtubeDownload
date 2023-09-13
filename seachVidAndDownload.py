from pytube import YouTube, Playlist,Search
import os



def downloadMp3(yt, askPath=0):
    # extract only audio
    video = yt.streams.filter(only_audio=True).first()

    destination = 'mp3File'
    # check for destination to save file
    if(askPath==1):
        print("Enter the destination (leave blank for default dir mp3File)")
        destination = str(input(">> ")) or 'mp3File'

    # download the file
    out_file = video.download(output_path=destination)

    # save the file
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)
    # result of success
    print(yt.title + " has been successfully downloaded.")



searchQuery = str(input("Search query ?"))
s = Search(searchQuery)
for index, vid in enumerate(s.results):
    print(f"{index}, Title: {vid.title}")
      
print('get result 0')
print(s.results[0].title)

downloadFlag = str(input("do you want to download? type index of song or type -1 to download all and n for abort: "))
if(downloadFlag=='-1'):
    for vid in s.results:
        print(vid)
        downloadMp3(vid)
elif(downloadFlag=='n'):
    exit()
else:
    downloadMp3(s.results[int(downloadFlag)])



