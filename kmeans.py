# import resource and display

# prepare data for k-means

# reshaps image into 2d array of pixels and 3 color values
pixel_vals= image_copy.reshape((-1,3))
# convert to float type
pixel_vals = np.float32(pixel_vals)

#implement k-means

#define stop criteria
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)

k = 2
retval, labels, centers = cv2.kmeans(pixel_vals, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

#convert data into 8-bit values
centers = .npuint8(centers)
segmented_data = centers[labels.flatten()]

segmented_image = segmented_data.reshape((image_copy.shape))
labels_reshape = labels.reshape(image_copy.shape[0], image_copy.shape[1])

#visualize one segment
plt.imshow(labels_reshape == 1, cmpa='gray')
