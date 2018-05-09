from PIL import Image, ImageDraw
import numpy as np
import datetime
import os
import time

while True:
	start = time.time()
	#Opening an image without libs
	name = "name"
	os.system("fswebcam -r 640x480 --no-banner "+name+".jpg")
	os.system("convert " + name + ".jpg -compress none " +name + ".ppm")

	image = Image.open(name+".jpg")
	im2 = np.array(image)
	end = time.time()
	print(end - start)
