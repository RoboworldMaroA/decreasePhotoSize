from PIL import Image
import os

# Marek Augustyn
# 12 Jan 2023
#Convert Vimeo format .webm to mp4

#directory to store files that you want to convert to format MP4
directoryWithVideos = 'directoryWithVideos'

# Loop thrue the all files in the folder with videos and convert this one that has extention .webm
for video in os.listdir(directoryWithVideos):
   
    print("This is videols"+video)
    # checking for hidden files named .DS_Store in the photos folder and ignoring them.
    if video=='.DS_Store':
       continue
    if (video.endswith(".webm")):
        #path to the video
        videoString = str(directoryWithVideos + "/"+video)
        #path to the place where will be save after convertion
        convertedVideo =str('directoryWithConvertedVideo'+"/"+os.path.basename(video.split('.')[0]))
        #Test only
        #print("This is video string  :" + videoString)
        #run a command in shell, using ffmpeg converst to the MP4
        #os.system(f"ffmpeg -i {videoString} -vcodec libx264 -crf 24 {convertedVideo}.mp4")
        os.system(f"ffmpeg -i {videoString} {convertedVideo}.mp4")
    else:
        continue
