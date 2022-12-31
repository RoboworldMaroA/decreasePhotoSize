from PIL import Image
import os
# Marek Augustyn
# 28.12.2022
# This aplication change the size of the photos to 720x500 px if you want a diffrent size adjust aprameters in the program
# Application that convert a files located in the folder photos on local drive
# Create folder where you want to keep aplication and go to the folder.
#  Use this comand before you run the app
#  Open Terminal (Install Python3)
#  Create a folder in Home directory
#  Create file newPhotoSize.py and paste this code below
#  python3 -m venv ~/pythonProjects
#  source ~/pythonProjects/bin/activate
#  python3 -m pip install --upgrade pip
#  python3 -m pip install --upgrade Pillow
#  
#  run program by: python newPhotoSize.py 
#  Photos from the folder photos will be saved to the folde smallphotos

directoryWithPhotos = 'photos'

# Go through the files in the photos folder and resize, make sure you have a copy of the original photos as they will be overwritten after resizing
for photo in os.listdir(directoryWithPhotos):
    f = os.path.join(directoryWithPhotos, photo)
    # checking for hidden files named .DS_Store in the photos folder and ignoring them.
    if photo=='.DS_Store':
       continue
    if os.path.isfile(f):
        #print(f)#test only
        image = Image.open(f)
        new_image = image.resize((720, 500))
        new_image.save('small'+f) 