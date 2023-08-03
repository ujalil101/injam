from PIL import Image
import os
from os import listdir
# python script to change all .webp files to jpg

# get the path/directory

folder_dir = "Test/Fake"
counter = 1
'''
for images in os.listdir(folder_dir):
    if images != ".DS_Store":
        im = Image.open("{}/{}".format(folder_dir,images))
        im.save("Image{}.jpg".format(counter),"jpeg")

'''
im = Image.open("/Users/ussie/Desktop/Injam/injam/Test/Fake/Image21.png")

im = im.convert('RGB')

 
im.save("Image21.jpg",quality=95)
'''
folder_dir = "Training/Real"
counter = 1
for images in os.listdir(folder_dir):
    os.rename("{}/{}".format(folder_dir,images), "Image{}.jpg".format(counter))
    counter+=1
'''

    