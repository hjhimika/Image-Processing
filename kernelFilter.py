import cv2
import numpy as np
img = cv2.imread(r"F:\testing_data\jpg_data\SampleJPGImage_20mbmb.jpg")
# Resize the image to fit within the screen (for example, 800x600 resolution)
image = cv2.resize(img, (1200,720))

# Show the resized image
cv2.imshow('Original Resized', image)

# Kernel blurring using filter2D()
# Making a kernel (I have explained what is a kernel below)
kernel_25 = np.ones((25,25),dtype=np.float32) / 625.0
# The ones function of numpy generates a matrix filled with ones of the 
# required size

# Apply kernel
output_kernel = cv2.filter2D(image,-1,kernel_25)

# blur function blurring same as above i.e., making a kernel and applying 
# it at once
output_blur = cv2.blur(image,(25,25))
# box filter
output_box = cv2.boxFilter(image,-1, (2,2),normalize=False)
# gaussian blur
output_gaussian = cv2.GaussianBlur(image,(25,25),sigmaX=0,sigmaY=0)
# median blur
output_median = cv2.medianBlur(image,5)
# bilateral blur
output_bilateral = cv2.bilateralFilter(image,5,sigmaColor=6,sigmaSpace=6)

# show the images using imshow funciton simple as it sounds
cv2.imshow('Original',image)
cv2.imshow('kernel blur',output_kernel)
cv2.imshow('blur',output_blur)
cv2.imshow('box filter',output_box)
cv2.imshow('gaussian blur',output_gaussian)
cv2.imshow('median blur',output_median)
cv2.imshow('bialteral filter',output_bilateral)
# This line makes the displayed windows wait for the user to close them
cv2.waitKey()
