from PIL import Image
import os
from os import listdir
# python script to change all .webp files to jpg

# get the path/directory
'''
folder_dir = "Training/Fake"
counter = 1
for images in os.listdir(folder_dir):
    if images != ".DS_Store":
        im = Image.open("{}/{}".format(folder_dir,images))
        im.save("Image{}.jpg".format(counter),"jpeg")
        counter+=1
'''
folder_dir = "Training/Real"
counter = 1
for images in os.listdir(folder_dir):
    os.rename("{}/{}".format(folder_dir,images), "Image{}.jpg".format(counter))
    counter+=1
    

    