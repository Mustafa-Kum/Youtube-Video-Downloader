from pytube import YouTube

youtubeLink = input("Link you want to download from YouTube : ")

youtube = YouTube(youtubeLink)

resolution = youtube.streams.get_highest_resolution()

print("Downloading...")

resolution.download()

print("Downloaded.")