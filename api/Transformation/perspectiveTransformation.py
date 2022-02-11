import numpy as np
import cv2
from Transformation.utils import plotImg, convertAsImg, convertAsMatrix
import base64


def clip(a, b):
    if a <= 0:
        return 0
    if a >= b - 1:
        return b - 1
    return a


def bilinearInterpolation(A, x, y):
    xMin = int(np.floor(x))
    yMin = int(np.floor(y))

    xMax = 1 + xMin
    yMax = 1 + yMin

    u = x - xMin
    v = y - yMin

    xMin = clip(xMin, A.shape[0])
    xMax = clip(xMax, A.shape[0])
    yMin = clip(yMin, A.shape[1])
    yMax = clip(yMax, A.shape[1])

    l = A[xMin, yMin]
    m = A[xMin, yMax]
    n = A[xMax, yMin]
    o = A[xMax, yMax]

    return (1.0 - u) * (1.0 - v) * l + u * (1.0 - v) * n + (1.0 - u) * v * m + u * v * o

def doCoeffCalculation(pt1, pt2, n):
    result = []
    pt2 = [pt2[0], pt2[1], 1]
    dimension = 3
    for i in range(dimension):
        curr = [0] * dimension * 4
        curr[i] = pt1[0]
        curr[dimension + i] = pt1[1]
        curr[2 * dimension + i] = 1 if i != 2 else 0

        curr[3 * dimension + n - 1] = -pt2[i]
        result.append(curr)

    return result


def doPerspectiveTransform(point1, point2):
    temp1 = []
    length = len(point1)
    for i in range(length):
        temp1 += doCoeffCalculation(point1[i], point2[i], i)

    temp2 = [0, 0, -1] * length
    value = np.linalg.solve(temp1, temp2)
    res = np.ones(9)
    res[:8] = value.flatten()[:8]
    return res.reshape(3, -1).T


def doWarpPerspective(img, val, destImg):
    mtr = convertAsMatrix(img)
    R, C = destImg
    dst = np.zeros((R, C,mtr.shape[2]))

    for i in range(mtr.shape[0]):
        for j in range(mtr.shape[1]):
            res = np.dot(val, [i, j, 1])
            i2, j2, _ = (res / res[2]+0.5).astype(np.int32)
            if 0 <= i2 < R:
                if 0 <= j2 < C:
                    dst[i2, j2] = bilinearInterpolation(mtr, i, j) 

    return convertAsImg(dst)

def increase_brightness(img, value=30):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)

    lim = 255 - value
    v[v > lim] = 255
    v[v <= lim] += value

    final_hsv = cv2.merge((h, s, v))
    img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
    return img

def perspectiveTransformation(inputImageName,parameters):
    image = cv2.imread('Transformation/Input_Images/'+inputImageName)
    # plotImg(image)
    # s = "350,200,965,30,790,1010,1430,800"
    #output = [[350, 200], [965, 30], [790, 1010], [1430, 800]]
    param_list = []
    # params = s.split(",")
    params = parameters.split(",")

    i = 0
    while i < len(params):
        param_list.append([int(params[i]),int(params[i+1])])
        i +=2

    # print(param_list)
    

    # sourceImgPoints = np.float32([[350, 200], [965, 30], [790, 1010], [1430, 800]])
    sourceImgPoints = np.float32(param_list)

    new_image = (image.shape[0], image.shape[1])
    destImgPoints = np.float32([[0, 0], [image.shape[0], 0], [0, image.shape[1]], [image.shape[0], image.shape[1]]])

    markerValues = doPerspectiveTransform(sourceImgPoints, destImgPoints)
    destination = doWarpPerspective(image, markerValues, new_image)
    # plotImg(destination)
    row = destination.shape[0]
    col = destination.shape[1]
    height = destination.shape[2]
    avg = 0
    for i in range(row):
        for j in range(col):
            for z in range(height):
                avg += destination[i][j][z]
    avg = avg / (row * col * height)

    for i in range(row):
        for j in range(col):
            for z in range(height):
                if destination[i][j][z] < 20:
                    destination[i][j][z] = avg

    i_img = np.zeros(destination.shape, np.uint8)

    for m in range(0,destination.shape[0]):
        for n in range(0,destination.shape[1]):
                i_img[m, n] = destination[m, n] * 0.6

    frame = increase_brightness(i_img, value=120)

    output_image_name = 'Transformation/Output_Images/'+inputImageName
    cv2.imwrite(output_image_name, frame)


    with open(output_image_name, "rb") as image_file:
        image_string = base64.b64encode(image_file.read())
        return image_string


if __name__ == "__main__":
    perspectiveTransformation("wimg.jpeg","a")
