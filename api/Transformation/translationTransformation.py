import numpy as np
import cv2
import base64
import math

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


def translate(image, alpha, beta):
    r, c,_ = image.shape
    M = np.float32([[1, 0, alpha], [0, 1, beta]])
    org = np.indices((c, r)).reshape(2, -1)
    norg = np.vstack((org, np.ones(r * c)))
    t = np.dot(M, norg)
    t = t.astype(np.int32)
    ind = np.all((t[1] < r, t[0] < c, t[1] >= 0, t[0] >= 0),axis=0)
    nimage = np.zeros_like(image)
    nimage[t[1][ind], t[0][ind]] = image[org[1][ind], org[0][ind]]

    img1 = np.zeros((nimage.shape[0], nimage.shape[1],3))
    for i in range(nimage.shape[0]):
        for j in range(nimage.shape[1]):
            img1[i,j] = bilinearInterpolation(nimage, i, j)

    return img1

def translationTransformation(inputImageName,parameters):
    image = cv2.imread('Transformation/Input_Images/'+inputImageName, cv2.IMREAD_COLOR)

    param_split = parameters.split(',')
    alpha = int(param_split[0].split("=")[1])
    beta = int(param_split[1].split("=")[1])
    print(alpha,beta)
    translated_image = translate(image,alpha=alpha, beta=beta)

    output_image_name = 'Transformation/Output_Images/'+inputImageName
    cv2.imwrite(output_image_name, translated_image)

    with open(output_image_name, "rb") as image_file:
        image_string = base64.b64encode(image_file.read())
        return image_string

if __name__ == "__main__":
    #Dog.jpg -a 125 -b 100
    translationTransformation("Dog.jpg","a=125,b=100")