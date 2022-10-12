from pytube import YouTube

VIDEO_URL = 'https://www.youtube.com/watch?v=8EJ3zbKTWQ8&list='
yt = YouTube(VIDEO_URL)

for stream in yt.streams:
    print(stream)