from pytubefix import Playlist
from pytubefix.cli import on_progress

url = "YOUTUBE URL"

pl = Playlist(url)
# i = 1
for video in pl.videos[:18]:     # first 5 videos
    ys = video.streams.get_highest_resolution()
    ys.download(output_path="./videos")
print("Done")