'''
Author: pw897

This module has a detect function that takes in an image and
returns coordinates of rectangles that contain a bug.

'''

import os
from PIL import Image
import numpy as np

#Returns the square distance
def distS3(x1,y1,z1,x2,y2,z2):
	return (x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2

#Returns the square distance
def distS2(x1,y1,x2,y2):
	return (x2-x1)**2 + (y2-y1)**2

class blob:
	'''A class for the bugs '''
	def __init__(self,x,y):
		self.minx = x
		self.miny = y
		self.maxx = x
		self.maxy = y
	def add(self,x,y):
		self.minx = min(self.minx,x)
		self.miny = min(self.miny,y)
		self.maxx = max(self.maxx, x)
		self.maxy = max(self.maxy, y)

	def isNear(self,x,y):
		cx = max(min(x,self.maxx),self.minx)
		cy = max(min(y,self.maxy),self.miny)
		d = distS2(cx,cy, x, y)
		if (d < 8**2): #If the point is in d should return false. 
			return True
		else:
			return False

	def __str__(self):
		return 'Blob at position ('+str(self.minx) +', '+ str(self.miny) +', '+ str(self.maxx) +', '+  str(self.maxy) +') '


def detect(im):
	blobs = []
	(height,width) = im.shape[0:2]
	print(height,width)
	for x in range(0,width):
	    for y in range(0,height):
			pixel = im[y][x]
			red = pixel[0]
			green = pixel[1]
			blue = pixel[2]
			d = distS3(red,green,blue,8,81,76)
			if(d < 5250):
				found = False
				for b in blobs:
					if(b.isNear(x,y)):
						b.add(x,y)
						found = True
						break;
				if(not found):
					newBlob = blob(x,y)
					blobs.append(newBlob)


	for i in blobs:
		if(i.miny == i.maxy):
			blobs.remove(i)
		if(i.minx == i.maxx):
			blobs.remove(i)


	#Checking if a blob is inside another blob 
	for i in blobs:
		for j in blobs:
			if (i == j):
				break
			else:
				#If i.minx is in js x range
				if(j.minx < i.maxx and j.minx > i.minx):
					if(j.miny < i.maxy and j.miny > i.miny):
						#print("i is inside j")
						blobs.remove(j)

				if(i.minx < j.maxx and i.minx > j.minx):
					if(i.miny < j.maxy and i.miny > j.miny):
						#print("j is inside i")
						blobs.remove(i)
	return blobs
