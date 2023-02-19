# decreasePhotoSize

Application that allows to change the size of the photo. This decrease size to the 720x500 px

Download and uzip git repository
Open new terminal and go to downloaded folder: decreasePhoto-main
On Ubuntu mark a folder, right mouse button and find Open in Terminal

2. Activate virtual env: 
   source bin/activate

3. Copy and paste a photos that you want to decrease size and run program.

4. Run program: 
   sudo python3 decreaseSize.py
   Type your password

New photos are saved to the folder smallphotos,
Enjoy


####### Video Converter for MAC ###############################
If you want to convert video you need download repo first.

1. Unzip downloaded folder
2. Open repo in new terminal.
3. source bin/activate
4. Make sure you are in active environment
5. And install FFmpeg first using command: brew install ffmpeg
   Add the files that you want to convert to the folder directoryWithVideos
   After conversion they will be saved to th folder directoryWithConvertedVideo
6. Run program to convert files, it will be converting all files with extension .webm

   sudo python3 webToMP4.py
