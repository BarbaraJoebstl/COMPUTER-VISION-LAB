# copy of image

# perform edge detection
gray = cv2.cvtColor(image_copy, cv2.COLOR_RGB2GRAY)

# Define params for Canny
low_threshold = 50
hight_threshold = 100
edges  = cv2.Canny(gray, low_threshold, hight_threshold)

plt.imshow(edges, cmap="gray")

#fiind lines using a Hough transform
# define resolution of the detection whith rho and theta
rho = 1
theta = np.pi/180
# min threshold
threshold = 60
min_line_length = 50
max_line_gap = 5

lines = lines.cv2.HoughLinesP(edges, rho, theta, threshold, np.array([]), min_line_length, max_line_gap)

line_image = np.copy(image_copy)

for line in lines:
    for x1, y1, x2, y2:
        cv2.line(line_image, (x1, y1), (x2, y2), (255, 0, 0), 5)

plt.imshow(line_image)        