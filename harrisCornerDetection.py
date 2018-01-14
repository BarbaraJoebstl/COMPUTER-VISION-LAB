import matplotlib.pyplot as plt
import numpy as np
import cv2

# Read in the image
image = cv2.imread('waffles.jpg')
# Convert it to RGB
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
# ---------------------------------------------------------- #


## Complete this corner detection function
## This takes in an image
## And returns dilated corners
def corner_detect(image):
    # Convert the image to grayscale, floating point values
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    gray = np.float32(gray)
    
    ## Create a Harris corner detector using those grayscale vals
    ## Change this value, but keep the variable name
    corners = cv2.cornerHarris(gray, 2, 3, 0.04)
    
    ## Dilate the corner detections
    corners = cv2.dilate(corners, None)
    
    # Return those values
    return corners

# Runs your function (do not change this line of code)
corners = corner_detect(image)

## Define a threshold to select strong corners
threshold = 0.1*corners.max()

# ---------------------------------------------------------- #
if(corners is not None):
    # Create an image copy to draw corners on
    corner_image = np.copy(image)

    # Iterate through all the corners and draw them on the image (if they pass the threshold)
    for j in range(0, corners.shape[0]):
        for i in range(0, corners.shape[1]):
            if(corners[j,i] > threshold):
                # image, center pt, radius, color, thickness
                cv2.circle(corner_image, (i, j), 1, (0,255,0), 1)      
                
    # Plot the result
    f, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 10))
    f.tight_layout()
    ax1.imshow(corners, cmap='gray')
    ax1.set_title('Dilated Corners')
    ax2.imshow(corner_image, cmap='gray')
    ax2.set_title('Thresholded Corners')