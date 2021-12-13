'''
Implementation of Region Growing
Reference: R. C. Gonzalez and R. E. Woods, "Digital Image Processing" Third edition, Pearson Education, 2009
'''

import cv2
from pylab import *

'''
Function: Accepts seed points to give the region grown out of the image.
Inputs: Image as numpy array
Returns: Output region image
'''


def growregion(temp_kernel, seed_pixel):
    row, col = np.shape(temp_kernel)
    region_grow_image = np.zeros((row + 1, col + 1))

    # print('temp kernel', temp_kernel.shape)
    # print('region_grow_image', region_grow_image.shape)
    swap = [seed_pixel[1], seed_pixel[0]]

    region_grow_image[swap[0]][swap[1]] = 255.0

    region_points = [[swap[0], swap[1]]]

    xp = [-1, 0, 1, -1, 1, -1, 0, 1]
    yp = [-1, -1, -1, 0, 0, 1, 1, 1]

    print('Running.. Please Wait..')
    c = 0
    while len(region_points) > 0:

        if c == 0:
            pt = region_points.pop(0)
            i = pt[0]
            j = pt[1]

        intensity = temp_kernel[i][j]
        low = intensity - 8
        high = intensity + 8
        for k in range(8):
            if region_grow_image[i + xp[k]][j + yp[k]] != 1:
                try:
                    if low < temp_kernel[i + xp[k]][j + yp[k]] < high:
                        region_grow_image[i + xp[k]][j + yp[k]] = 1
                        px = [0, 0]
                        px[0] = i + xp[k]
                        px[1] = j + yp[k]
                        if px not in region_points:
                            if 0 < px[0] < row and 0 < px[1] < col:
                                region_points.append([i + xp[k], j + yp[k]])
                                print('Added Region: ', [i + xp[k], j + yp[k]])
                    else:
                        region_grow_image[i + xp[k]][j + yp[k]] = 0
                except IndexError:
                    continue

        pt = region_points.pop(0)
        i = pt[0]
        j = pt[1]
        c = c + 1

    print('Region addition completed')
    return region_grow_image


'''
Function: Accepts image path (Gray scale image or it does).
Inputs: Image Path
Returns: Segmented Region Grown Image
'''


def regionSeg(path):
    image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    temp_kernel = np.asarray(image)

    plt.figure()
    plt.title('Input Image\nSelect a seed point to segment a region')
    plt.imshow(image)
    plt.gray()

    print('Click on the region to grow')

    seed_point = plt.ginput(1)
    x = int(seed_point[0][0])
    y = int(seed_point[0][1])

    seed_pixel = [x, y]
    print('Seed Points: ', seed_pixel)
    plt.close()

    region_grow_image = growregion(temp_kernel, seed_pixel)

    plt.figure()
    plt.title('Resulted Segmented Image')
    plt.imshow(region_grow_image, cmap="gray")
    plt.show()


'''
Function: Accepts image path (Color Images).
Inputs: Image Path
Returns: Segmented Region Grown Image
'''


def colorRegionSeg(path):
    # Tried with YCbCr and HSV color models but the size of the\
    # image is reduced abruptly and selection of seed  points becomes\
    # difficult (selected in new range). So sticked with RGB model itself, results are satisfactory\
    # than above models.

    # Implementing YCbCr and HSV is same and we maintained dynamic change\
    # to try  YCbCr or HSV uncomment the codes and comment the RGB part to\
    # test the code.

    image = cv2.imread(path)
    (B, G, R) = cv2.split(image)

    # image = cv2.imread(path, cv2.COLOR_BGR2YCrCb)
    # (Y, Cr, Cb) = cv2.split(image)

    plt.figure()
    plt.title('Input Image\nSelect a seed point to segment a region')
    plt.imshow(image)
    plt.gray()

    print('Click on the region to grow')

    seed_point = plt.ginput(1)
    x = int(seed_point[0][0])
    y = int(seed_point[0][1])

    seed_pixel = [x, y]
    print('Seed Points: ', seed_pixel)
    plt.close()

    temp_kernel1 = np.asarray(R)
    temp_kernel2 = np.asarray(G)
    temp_kernel3 = np.asarray(B)

    Rregion = growregion(temp_kernel1, seed_pixel)
    Gregion = growregion(temp_kernel2, seed_pixel)
    Bregion = growregion(temp_kernel3, seed_pixel)

    region_grow_image = cv2.merge([Bregion, Gregion, Rregion])

    # temp_kernel1 = np.asarray(Y)
    # temp_kernel2 = np.asarray(Cb)
    # temp_kernel3 = np.asarray(Cr)

    # Yregion = growregion(temp_kernel1, seed_pixel)
    # Cbregion = growregion(temp_kernel2, seed_pixel)
    # Crregion = growregion(temp_kernel3, seed_pixel)

    # region_grow_image = cv2.merge([Yregion, Cbregion, Crregion]) #Or
    # region_grow_image = Yregion

    plt.figure()
    plt.title('Resulted Segmented Image')
    plt.imshow(region_grow_image)
    plt.show()


'''
Main function.
Change the path to accept images (Accepted: .jpg, .jpeg, .png, .bmp)
'''
path = "/Users/rajeshr/Desktop/ProjectDIP/shapes.jpeg"

# Uncomment for gray scale processing or Comment for color image. (Preferred this)
regionSeg(path)

# Uncomment for color image and Comment for gray scale images
# colorRegionSeg(path)
