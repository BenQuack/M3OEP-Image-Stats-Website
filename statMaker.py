import matplotlib.pyplot as plt
import cv2
import sys

import numpy as np

fileName = "side_eye_cat.jpg"

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
for r in range(len(rValues)):
    avgRValue += rValues[r]

avgRValue = avgRValue / len(rValues)

avgGValue = 0
for g in range(len(gValues)):
    avgGValue += gValues[g]

avgGValue = avgGValue / len(gValues)

avgBValue = 0
for b in range(len(bValues)):
    avgBValue += bValues[b]

avgBValue = avgBValue / len(bValues)

print(avgRValue)
print(avgGValue)
print(avgBValue)

#calculates the most seen values of red green and blue
rValueCounts = []
gValueCounts = []
bValueCounts = []
for x in range(255):
    rValueCounts.append(0)
    gValueCounts.append(0)
    bValueCounts.append(0)

for r in rValues:
    rValueCounts[r - 1] = rValueCounts[r - 1] + 1
    print(r)

for g in rValues:
    gValueCounts[g - 1] = gValueCounts[g - 1] + 1

for b in rValues:
    bValueCounts[b - 1] = bValueCounts[b - 1] + 1

#plots the counts of each rgb occurrence
rSpace = range(1,256)
gSpace = range(6,261)
bSpace = range(11,266)

ax = plt.subplot(111)

if rValueCounts == gValueCounts == bValueCounts:
    print('match')

#TODO:fix plots 
ax.plot(rSpace, rValueCounts, label = "red")
ax.plot(rSpace, gValueCounts, label = "green")
ax.plot(rSpace, bValueCounts, label = "blue")



plt.gcf().canvas.manager.set_window_title('Speed Test')
# Set the graph title
plt.title('Color occurrence')
# Label the x axis
plt.xlabel('RGB value')
# Make sure the x-axis tick marks/labels are at each 1000
plt.xticks(range(1,256))
# Label the y axis
plt.ylabel('number of occurrence')

plt.savefig("RGB_occurrences.png")

