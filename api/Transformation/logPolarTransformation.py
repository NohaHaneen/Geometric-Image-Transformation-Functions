import cv2
import numpy as np
import matplotlib.pyplot as plt
import base64

def clip(a, b):
    if a <= 0:
        return 0
    if a >= b - 1:
        return b - 1
    return a


def lpBilinearInterpolation(A, x, y):
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


def toPolar(A, B, C, X, Y, Rmin, Rmax):
    transformedImage = np.zeros((B, C)) if len(A.shape) == 2 else np.zeros((B, C, A.shape[2]))
    di = (np.log(Rmax) - np.log(Rmin)) / B
    dj = 2.0 * np.pi / C

    for i in range(B):
        for j in range(C):
            t = Rmin * np.exp(di * i)
            p = dj * j
            x = X + t * np.cos(p)
            y = Y + t * np.sin(p)
            transformedImage[i, j] = lpBilinearInterpolation(A, x, y)

    return transformedImage


def logPolarTransformationService(image):
    A = image / 255.0
    B = 64
    C = 90
    X = 0.5 + A.shape[0] / 2
    Y = 0.5 + A.shape[1] / 2
    Rmin = 0.1
    Rmax = np.linalg.norm(np.array([X, Y]))

    transformedImage = toPolar(A, B, C, X, Y, Rmin, Rmax)
    # plt.imshow(transformedImage)
    # plt.show()
    return transformedImage * 255.0
   


def logPolarTransformation(inputImageName,parameters):
    # image = cv2.imread("lena.jpg")
    image = cv2.imread('Transformation/Input_Images/'+inputImageName, cv2.IMREAD_COLOR)
    transformedImage = logPolarTransformationService(image)
    # transformedImage = transformedImage 
    output_image_name = 'Transformation/Output_Images/'+inputImageName
    cv2.imwrite(output_image_name, transformedImage)
    with open(output_image_name, "rb") as image_file:
        image_string = base64.b64encode(image_file.read())
        return image_string


if __name__ == "__main__":
    logPolarTransformation("lena.jpg","as")
