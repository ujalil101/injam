from PIL import Image
import os
from os import listdir
# python script to change all .webp files to jpg

# get the path/directory

folder_dir = "Fake"
counter = 103

'''

for images in os.listdir(folder_dir):
    if images != ".DS_Store":
       
        im = Image.open("{}/{}".format(folder_dir,images)).convert("RGB")
        im.save("Image{}.jpg".format(counter),"jpeg")
        counter += 1
'''



for images in os.listdir(folder_dir):
    os.rename("{}/{}".format(folder_dir,images), "Image{}.jpg".format(counter))
    counter+=1


    