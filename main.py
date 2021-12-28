# importing packages
from pytube import Channel
import os
  
# url input from user
yt = str(input("Enter the URL of the channel you want to download the mp3 from: \n>> "))
  
# extract only audio
c = Channel(yt)

# video = yt.streams.filter(only_audio=True).first()
  
# check for destination to save file
print("Enter the destination (leave blank for current directory)")
destination = str(input(">> ")) or '.'

# download the file
cnt = 0
for video in c.videos:
  # download the file
  out_file = video.streams.filter(only_audio=True).first().download(output_path=destination)

  # save the file
  base, ext = os.path.splitext(out_file)
  new_file = base + '.mp3'
  os.rename(out_file, new_file)

  # result of success
  print(f'"{video.title}" has been successfully downloaded')
  cnt += 1

# endresult of downloaded videos
print(f'{cnt} videos have been sucessfully downloaded')