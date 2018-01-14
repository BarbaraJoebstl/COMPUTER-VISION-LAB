import numpy as np
import matplotlib.pyplot as plt
import cv2

# Read in the image
image = cv2.imread('license_plate_skew.jpg')
# Convert to RGB (from BGR)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
# ---------------------------------------------------------- #
## TODO: Define the geometric tranform function
## This function take in an image and returns a 
## geometrically transformed image

def geo_tx(image):
    image_size = (image.shape[1], image.shape[0])
    
    ##  Define the four source coordinates
    ## use: plt.qt to get the points easier
    ## always: start top left, then counter clockwise
    source_pts = np.float32(
        [[350, 800],
         [350, 1000],
         [550, 1000],
         [550, 850]])
    
    ## Define the four destination coordinates    
    ## Tip: These points should define a 400x200px rectangle
    warped_pts = np.float32(
        [[500, 800],
         [500, 1000],
         [900, 1000],
         [900, 800]])
    
    ## Compute the perspective transform, M
    M = cv2.getPerspectiveTransform(source_pts, warped_pts)
    
    ## Using M, create a warped image named `warped`
    warped = cv2.warpPerspective(image, M, image_size, flags=cv2.INTER_LINEAR)

    return warped
    
    
# ---------------------------------------------------------- #
# Make a copy of the original image and warp it
warped_image = np.copy(image)
warped_image = geo_tx(warped_image)

if(warped_image is not None):
    # Visualize
    f, (ax1, ax2) = plt.subplots(1, 2, figsize=(20,10))
    ax1.set_title('Source image')
    ax1.imshow(image)
    ax2.set_title('Warped image')
    ax2.imshow(warped_image)
else:
    print('No warped image was returned by your function.')
