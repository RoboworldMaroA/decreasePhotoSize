# decreasePhotoSize

Application that allows to change the size of the photo. This decrease size to the 720x500 px

Download and uzip git repo
Open new terminal and go to downloaded folder: decreasePhoto-main
Activate virtual env: source bin/activate
Copy and paste a photos that you want to decrease size and run program.
Run program: python3 decreaseSize.py

New photos are saved to the folder smallPhotos

If you want to convert video you need download repo first.

1. Unzip downloaded folder
2. Open repo in new terminal.
3. source bin/activate
4. Make sure you are in active enironment
5. And install FFmpeg first using command: brew install ffmpeg
   Add the files that you want to convert to the folder directoryWithVideos
   After convertion they will be saved to th folder directoryWithConvertedVideo
6. Run program to convert files, it will be converting all files with extention .webm
   python3 webToMP4.py
