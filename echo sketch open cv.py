#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import cv2
import matplotlib.pyplot as plt
img = cv2.imread("echo.jpg")

def sketch_image(photo, k_size):
    #Read Image
    img=cv2.imread('echo.jpg')
    
    # Convert to Grey Image
    grey_img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Invert Image
    invert_img=cv2.bitwise_not(grey_img)
    #invert_img=255-grey_img

    # Blur image
    blur_img=cv2.GaussianBlur(invert_img, (k_size,k_size),0)

    # Invert Blurred Image
    invblur_img=cv2.bitwise_not(blur_img)
    #invblur_img=255-blur_img

    # Sketch Image
    sketch_img=cv2.divide(grey_img,invblur_img, scale=256.0)

    # Save Sketch 
    cv2.imwrite('sketch.png', sketch_img)

    # Display sketch
    cv2.imshow('sketch image',sketch_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
#Function call
sketch_image(photo='image_1.png', k_size=7)


# In[ ]:




