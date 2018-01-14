'''
Gaussian blur

'''

#convert image to gray
#filter 5x5 bigger filter -> bigger blur
gray_blur = cv2.GaussianBlur(gray, (5,5), 0)

'''
CANNY EDge DEtector
'''

# gray = convert to grayscale

# define lower and upper threshold for hysteresis
# use 1:2 or 1:3
lower = 120
upper = 240

edges= cv2.Canny(gray, lower, upper)
