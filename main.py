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
  out_file_mp4 = video.streams.filter(only_audio=True).first().download(output_path=destination)
  out_file_mp3 = out_file_mp4.replace('mp4', 'mp3')

  # convert the file
  cmd = f'ffmpeg -i "{out_file_mp4}" -vn "{out_file_mp3}"'
  os.system(cmd)

  # remove the old file
  os.remove(out_file_mp4)

  # result of success
  print(f'"{video.title}" has been successfully downloaded')
  cnt += 1

# endresult of downloaded videos
print(f'{cnt} videos have been sucessfully downloaded')