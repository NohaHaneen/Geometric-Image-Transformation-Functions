import cv2
import numpy as np
import math
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


def polarTransformationService(image):
    h = image.shape[0]
    w = image.shape[1]
    yMid = h / 2
    xMid = w / 2
    R = math.sqrt(xMid * xMid + yMid * yMid)
    R = int(R)
    transformedImage = np.zeros((R, 300, 3))

    for i in range(R):
        for j in range(300):
            theta = j * math.pi / 150
            x = xMid + i * math.cos(theta)
            y = yMid + i * math.sin(theta)
            x = int(x)
            y = int(y)

            if 0 <= x < w and 0 <= y < h:
                transformedImage[i][j] = bilinearInterpolation(image, y, x)

    transformedImage = transformedImage.astype(int)

    return transformedImage


def polarTransformation(inputImageName,parameters):
    # image = cv2.imread("wimg.jpeg")
    image = cv2.imread('Transformation/Input_Images/'+inputImageName, cv2.IMREAD_COLOR)
    image = np.array(image)

    transformedImage = polarTransformationService(image)

    output_image_name = 'Transformation/Output_Images/'+inputImageName
    cv2.imwrite(output_image_name, transformedImage)

    with open(output_image_name, "rb") as image_file:
        image_string = base64.b64encode(image_file.read())
        return image_string

if __name__ == "__main__":
    polarTransformation()
