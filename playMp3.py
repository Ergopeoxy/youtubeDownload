
filename = str(input("what is the name of the file you want to play?"))

import os

path = os.path.abspath("mp3File/"+filename)

import webbrowser
webbrowser.open(path)

# p = vlc.MediaPlayer("mp3File/"+filename)
# p.play()