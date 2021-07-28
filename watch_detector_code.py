# importing the required libraries
import numpy as np
import cv2

# loading the self trained cascade .xml file as 'watch_cascade'
watch_cascade = cv2.CascadeClassifier('C:/Users/rajen/Desktop/OpenCV Project/watch_cascade.xml')

# reading the testing image as 'img'
img = cv2.imread('C:/Users/rajen/Desktop/OpenCV Project/watch_test1.jpg')

## for converting the color image to grey scale image directly at the time of reading
#grey = cv2.imread('C:/Users/rajen/Desktop/OpenCV Project/watch_test0.jpg',0)

# for converting color image to grey scale after reading color image as 'img'
grey = cv2.cvtColor(img,0)

# storing all the watches in the image into 'watches'
watches = watch_cascade.detectMultiScale(grey,1.01,8)

# for each watch in watches we draw a rectangle around it
for (x,y,w,h) in watches:
    img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

# for showing the detected image with rectangle around the watch
cv2.imshow('detected_img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
