
# OpenCV program to perform Edge detection in real time 
# import libraries of python OpenCV  
# where its functionality resides 
import cv2  
  
# np is an alias pointing to numpy library 
import numpy as np
from matplotlib import pyplot as plt

  
  
# capture frames from a camera 
frame = cv2.imread('image.jpg')
# loop runs if capturing has been initialized 

  
    # reads frames from a camera 
# {ret, frame = cap.read() 

# converting BGR to HSV 
hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) 
  
# define range of red color in HSV 
lower_red = np.array([30,150,50]) 
upper_red = np.array([255,255,180]) 
  
# create a red HSV colour boundary and  
# threshold HSV image 
mask = cv2.inRange(hsv, lower_red, upper_red) 

# Bitwise-AND mask and original image 
res = cv2.bitwise_and(frame,frame, mask= mask) 

# Display an original image 
cv2.imshow('Original',frame) 

# finds edges in the input image image and 
# marks them in the output map edges 
edges = cv2.Canny(frame,100,200) 

# Display edges in a frame 
cv2.imshow('Edges',edges) 
plt.subplot(121),plt.imshow(frame),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges),plt.title('Result')
plt.xticks([]), plt.yticks([])
plt.show()
# Wait for Esc key to stop 
# k = cv2.waitKey(5) & 0xFF

  
# Close the window 
# cap.release() 
  
# De-allocate any associated memory usage 
# cv2.destroyAllWindows()  
