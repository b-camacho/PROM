from PIL import Image, ImageDraw
import numpy as np
import bugDetect
import datetime

#Opening the image
#image = Image.open("3bugs.jpg")
image = Image.open("gets2.jpg")
im2 = np.array(image)
blobs = []
bugs = bugDetect.detect(im2)

if not(len(bugs) == 0):
	print(len(bugs),'Bugs Detected')
	print("Image: Cockroach Detected")
	now = datetime.datetime.now()
	print now.strftime("%Y-%m-%d %H:%M")
	draw = ImageDraw.Draw(image)
	for bug in bugs:
		print(bug)
		draw.rectangle([bug.minx,bug.miny,bug.maxx,bug.maxy],fill=None,outline=(255,0,0))
	image.save(now.strftime("%Y-%m-%d %H:%M")+".ppm")