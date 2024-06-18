from sys import argv
from pytube import YouTube
"""
argv module from sys library allows us to capture the link from the command line when running the file
pytube is the library that will allow us to capture and manipulate info from YouTube
"""
#Takes the link from the command line
link = argv[1]

yt = YouTube(link)

#Double Checking that we downloaded the correct video
print("Title: ", yt.title)
print("Views: ", yt.views)

yd = yt.streams.get_highest_resolution()

#The argument in the download method is the path you want the file to be downloaded at
yd.download('')