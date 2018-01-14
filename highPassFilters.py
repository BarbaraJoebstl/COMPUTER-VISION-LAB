'''
Edge Handling
Kernel convolution relies on centering a pixel and looking at it's surrounding neighbors. So, what do you do if there are no surrounding pixels like on an image corner or edge? Well, there are a number of ways to process the edges, which are listed below. It’s most common to use extension or cropping, and in these OpenCV examples, we will use the default technique, which is extension. In extension, the border pixels of an image are copied and extended far enough to result in a filtered image of the same size as the original image.

Extend The nearest border pixels are conceptually extended as far as necessary to provide values for the convolution. Corner pixels are extended in 90° wedges. Other edge pixels are extended in lines.

Wrap The image is conceptually wrapped (or tiled) and values are taken from the opposite edge or corner.

Crop Any pixel in the output image which would require values from beyond the edge is skipped. This method can result in the output image being slightly smaller, with the edges having been cropped.
'''

'''
Sobel filters
The Sobel filter is very commonly used in edge detection and in finding patterns in intensity in an image. Applying a Sobel filter to an image is a way of taking (an approximation) of the derivative of the image in the xx or yy direction. The operators for Sobel_xSobel 
x
​	  and Sobel_ySobel 
y
​	 , respectively, look like this:


Sobel filters

Next, let's see an example of these two filters applied to an image of the brain.


Sobel x and y filters (left and right) applied to an image of a brain

xx vs. yy
In the above images, you can see that the gradients taken in both the xx and the yy directions detect the edges of the brain and pick up other edges. Taking the gradient in the xx direction emphasizes edges closer to vertical. Alternatively, taking the gradient in the yy direction emphasizes edges closer to horizontal.

Magnitude
Sobel also detects which edges are strongest. This is encapsulated by the magnitude of the gradient; the greater the magnitude, the stronger the edge is. The magnitude, or absolute value, of the gradient is just the square root of the squares of the individual x and y gradients. For a gradient in both the xx and yy directions, the magnitude is the square root of the sum of the squares.

abs_sobelx = \sqrt{(sobel_x)^2}= 
(sobel 
x
​	 ) 
2
 
​	 

abs_sobely = \sqrt{(sobel_y)^2}= 
(sobel 
y
​	 ) 
2
 
​	 

abs_sobelxy = \sqrt{(sobel_x)^2+(sobel_y)^2}= 
(sobel 
x
​	 ) 
2
 +(sobel 
y
​	 ) 
2
 
​	 

Direction
In many cases, it will be useful to look for edges in a particular orientation. For example, we may want to find lines that only angle upwards or point left. By calculating the direction of the image gradient in the x and y directions separately, we can determine the direction of that gradient!

The direction of the gradient is simply the inverse tangent (arctangent) of the yy gradient divided by the xx gradient:

tan^{-1}{(sobel_y/sobel_x)}tan 
−1
 (sobel 
y
​	 /sobel 
x
​	 ).

Later, we'll see exactly how the magnitude and direction of an image gradient can be used in current applications. Let's keep learning!

'''

# get image
# convert to bgr
# make copy of image

# then:
gray = cv2.cvtColor(image_copy, cv2.COLOR_RGB2GRAY)
plt.imshow(gray, cmap="gray")

#create a custom kernel 3x3
# to detect vertical edges
# common filter which is called sobel filter
sobel_x = np.array([[-1,0, 1], 
[-2,0, 2 ],
 [-1, 0, 1]
])

filtered_image = cv2.filter2D(gray, -1, sobel_x)
plot.imshow(filtered_image, cmpa="gray")

#create a binary image
retval, binary_image = cv2.treshold(filtered_image, 100, 255, cv2.THRESH_BINARY)
plot.imshow(binary_image, cmpa="gray")

