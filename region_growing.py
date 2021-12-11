import cv2
from pylab import *


def growregion(temp_kernel, seed_pixel):
    row, col = np.shape(temp_kernel)
    region_grow_image = np.zeros((row + 1, col + 1))

    print('temp kernel', temp_kernel.shape)
    print('region_grow_image', region_grow_image.shape)
    swap = [seed_pixel[1], seed_pixel[0]]

    region_grow_image[swap[0]][swap[1]] = 255.0

    region_points = [[swap[0], swap[1]]]

    xp = [-1, 0, 1, -1, 1, -1, 0, 1]
    yp = [-1, -1, -1, 0, 0, 1, 1, 1]

    print('Running.. Please Wait..')
    count = 0
    while len(region_points) > 0:

        if count == 0:
            point = region_points.pop(0)
            i = point[0]
            j = point[1]

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

        point = region_points.pop(0)
        i = point[0]
        j = point[1]
        count = count + 1

    print('Region addition completed')
    return region_grow_image


def regionSeg(path):
    image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    temp_kernel = np.asarray(image)

    plt.figure()
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
    plt.imshow(region_grow_image, cmap="Greys_r")
    plt.colorbar()
    plt.show()


path = "/Users/rajeshr/Desktop/ProjectDIP/shapes.jpeg"
regionSeg(path)
