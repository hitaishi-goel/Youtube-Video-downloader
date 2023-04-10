import os
from pytube import YouTube
from time import time
from tkinter import *
from customtkinter import *
# Initialize all the settings
set_appearance_mode("System") # Setting the appearance mode to follow by the app: "System", "Light" or "Dark"
set_default_color_theme("blue")
 # Setting the theme of the app to follow
for i in os.listdir(os.getcwd()):
    if i == "youtube_downloads": 
# If there's already a folder called "youtube_downloads", do not create a new one
        break
else:    
    os.mkdir("youtube_downloads") # If there is no folder called "youtube_downloads", create a new one
def Download_video(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
    except:
        print("An error has occurred")
    print("Download is completed successfully")
def Download_audio(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_audio_only()
    try:
        youtubeObject.download()
    except:
        print("An error has occurred")
    print("Download is completed successfully")
master = CTk()
p1 = PhotoImage(file = 'ico.png')
  
# Setting icon of master window
master.iconphoto(master, p1)
master.title("YouTube Downloader")
master.grid_rowconfigure((0,1), weight=1)
master.grid_columnconfigure((0,1), weight=1)
master.geometry("350x350")
master.resizable(False, False)
CTkLabel(master, text="Enter YouTube video URL:").grid(row=0, column=0)
entry = CTkEntry(master)
entry.grid(row=0, column=1)
CTkButton(master, text='Download Audio', command=lambda *args: Download_audio(entry.get())).grid(row=1, column=0, columnspan=1)
CTkButton(master, text='Download Video', command=lambda *args: Download_video(entry.get())).grid(row=1, column=1, columnspan=1)
master.mainloop()