from pytubefix import Playlist
from pytubefix.cli import on_progress

url = "https://www.youtube.com/watch?v=tVzUXW6siu0&list=PLu0W_9lII9agq5TrH9XLIKQvv0iaF2X3w"

pl = Playlist(url)
# i = 1
for video in pl.videos[:18]:     # first 5 videos
    ys = video.streams.get_highest_resolution()
    ys.download(output_path="./videos")
print("Done")