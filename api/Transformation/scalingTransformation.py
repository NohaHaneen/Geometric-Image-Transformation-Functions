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


def intensity_scaling(input_image, column, alpha, beta):
    i_img = np.zeros(input_image.shape, np.uint8)

    for m in range(0,input_image.shape[0]):
        for n in range(0,input_image.shape[1]):
            if n < column:
                i_img[m, n] = bilinearInterpolation(input_image, m, n) * alpha
            else:
                i_img[m, n] = bilinearInterpolation(input_image, m, n) * beta
    return i_img


def scalingTransformation(inputImageName,parameters):
    image = cv2.imread('Transformation/Input_Images/'+inputImageName, cv2.IMREAD_COLOR)

    param_split = parameters.split(',')
    column = int(param_split[0].split("=")[1])
    alpha = float(param_split[1].split("=")[1])
    beta = float(param_split[2].split("=")[1])
    # print(column,alpha,beta)

    scaled_image = intensity_scaling(image, column=column, alpha=alpha, beta=beta)

    output_image_name = 'Transformation/Output_Images/'+inputImageName
    cv2.imwrite(output_image_name, scaled_image)

    with open(output_image_name, "rb") as image_file:
        image_string = base64.b64encode(image_file.read())
        return image_string

if __name__ == "__main__":
    #Dog.jpg -c 255 -a 0.2 -b 0.8
    scalingTransformation("Dog.jpg","c=255,a=0.2,b=0.8")