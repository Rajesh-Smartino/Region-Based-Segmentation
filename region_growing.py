from PIL import Image
from pylab import *
from pylab import *
import cv2

image = cv2.imread("/Users/rajeshr/Desktop/ProjectDIP/view4.png", cv2.IMREAD_GRAYSCALE)
temp_kernel = np.asarray(image)

# hsv_image = cv2.imread("/Users/rajeshr/Desktop/ProjectDIP/peppers.png", cv2.COLOR_BGR2HSV)
# image = hsv_image[:, :, 0]
# temp_kernel = np.asarray(image)

row, col = np.shape(temp_kernel)
plt.figure()
plt.imshow(image)
plt.gray()

seed_point = plt.ginput(1)
x = int(seed_point[0][0])
y = int(seed_point[0][1])
seed_pixel = [x, y]

print('you clicked:', seed_pixel)
plt.close()