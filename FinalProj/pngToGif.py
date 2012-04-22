#!usr/local/bin/python
# /Users/mcdickenson/github/PS398/FinalProj/
# png to gif

from PIL import Image as pilImage
from PIL import ImageTk as pilImageTk

def pngToGif(filename):
	tempPic = pilImage.open(filename+'.png')
        tempPic = tempPic.convert('RGB').convert('P', palette=pilImage.ADAPTIVE)
        tempPic.save(filename+'.gif')
