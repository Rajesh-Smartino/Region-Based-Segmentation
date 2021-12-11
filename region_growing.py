import cv2
from pylab import *


def growregion(temp_kernel, seed_pixel):
    row, col = np.shape(temp_kernel)
    region_grow_image = np.zeros((row + 1, col + 1))
    region_grow_image[seed_pixel[0]][seed_pixel[1]] = 255.0

    region_points = [[seed_pixel[0], seed_pixel[1]]]

    count = 0
    x = [-1, 0, 1, -1, 1, -1, 0, 1]
    y = [-1, -1, -1, 0, 0, 1, 1, 1]

    while len(region_points) > 0:
        if count == 0:
            point = region_points.pop(0)
            i = point[0]
            j = point[1]
            print('i and j:', i, j)
        print('\nRunning.. Please Wait..')
        intensity = temp_kernel[i][j]
        low = intensity - 8
        high = intensity + 8
        for k in range(8):
            if region_grow_image[i + x[k]][j + y[k]] != 1:
                try:
                    if low < temp_kernel[i + x[k]][j + y[k]] < high:
                        region_grow_image[i + x[k]][j + y[k]] = 1
                        p = [0, 0]
                        p[0] = i + x[k]
                        p[1] = j + y[k]
                        if p not in region_points:
                            if 0 < p[0] < row and 0 < p[1] < col:
                                ''' adding points to the region '''
                                region_points.append([i + x[k], j + y[k]])
                                print('Added Region: ', [i + x[k], j + y[k]])
                    else:
                        region_grow_image[i + x[k]][j + y[k]] = 0

                except IndexError:
                    continue

        point = region_points.pop(0)
        i = point[0]
        j = point[1]
        count = count + 1

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


path = "/Users/rajeshr/Desktop/ProjectDIP/rgb_shapes.jpeg"
regionSeg(path)
