import matplotlib.pyplot as plt
import cv2
import sys

import numpy as np

fileName = sys.argv[1]

img = cv2.imread(fileName)

dimensions = img.shape
colorValues = []
rValues = []
gValues = []
bValues = []
for x in range(dimensions[0]):
    for y in range(dimensions[1]):
        rValues.append(img[x,y][0])
        gValues.append(img[x,y][1])
        bValues.append(img[x,y][2])

#calculates the average red green and blue value of
#the image
avgRValue = 0
for r in range(rValues):
    avgRValue += rValues[r]

avgRValue = avgRValue / len(rValues)

avgGValue = 0
for g in range(gValues):
    avgGValue += gValues[g]

avgGValue = avgGValue / len(gValues)

avgBValue = 0
for b in range(bValues):
    avgBValue += bValues[b]

avgBValue = avgBValue / len(bValues)

#calculates the most seen values of red green and blue

rValueCounts = []
for r in rValues:
    rValueCounts[r] = rValueCounts + 1

gValueCounts = []
for g in rValues:
    gValueCounts[g] = rValueCounts + 1

bValueCounts = []
for b in rValues:
    bValueCounts[b] = rValueCounts + 1