import numpy as np
import cv2
from Transformation.utils import plotImg, convertAsImg, convertAsMatrix
import base64


def affineTransformationService(image, sourcePoints, destPoints):
    temp = []
    for i, j in sourcePoints:
        temp.append((i, j, 1))
    resultPoint = np.linalg.solve(temp, destPoints).T
    newImage = (image.shape[1], image.shape[0])
    transformedImage = dowarpAffine(image, resultPoint, newImage)

    return transformedImage


def dowarpAffine(img, val, newImg):
    imgMatrix = convertAsMatrix(img)
    R, C = newImg
    dst = np.zeros((R, C, imgMatrix.shape[2]), dtype='int')

    for i in range(imgMatrix.shape[0]):
        for j in range(imgMatrix.shape[1]):
            i_dst, j_dst = np.dot(val, [i, j, 1]).astype(int)
            if 0 <= i_dst < R:
                if 0 <= j_dst < C:
                    dst[i_dst, j_dst] = imgMatrix[i, j]

    img_nn = np.zeros((R, C, 3))
    for i_prime in range(dst.shape[0]):
        for j_prime in range(dst.shape[1]):
            i, j = np.dot(val, [i_prime, j_prime, 1]).astype(int)

            i_NN = round(i)
            j_NN = round(j)

            if round(i) < img.shape[0] and round(j) < img.shape[1] and round(i) >= 0 and round(j) >= 0:
                img_nn[i_prime, j_prime] = nearest_neighbors(i, j, imgMatrix, val)

    return convertAsImg(img_nn)

# nearest neighbors interpolation
def nearest_neighbors(x, y, M, val):
    x_max, y_max = M.shape[0] - 1, M.shape[1] - 1
    if np.abs(np.floor(x) - x) < np.abs(np.ceil(x) - x):
        x = int(np.floor(x))
    else:
        x = int(np.ceil(x))
    if np.abs(np.floor(y) - y) < np.abs(np.ceil(y) - y):
        y = int(np.floor(y))
    else:
        y = int(np.ceil(y))
    if x > x_max:
        x = x_max
    if y > y_max:
        y = y_max
    if np.floor(x) == x and np.floor(y) == y:
        x, y = int(x), int(y)
        return M[x, y]
    return M[x, y]

def affineTransformation(inputImageName,parameters):
    # image = cv2.imread('wimg.jpeg', cv2.IMREAD_COLOR)
    image = cv2.imread('Transformation/Input_Images/'+inputImageName, cv2.IMREAD_COLOR)

    # s="src=50,50,200,50,50,200;dst=10,100,200,50,100,250"
    src_param_list = []
    dst_param_list = []
    # params = s.split(";")
    params = parameters.split(";")
    src_params = params[0].split("=")[1].split(",")
    dst_params = params[1].split("=")[1].split(",")
    src_params = list(map(int,src_params))
    dst_params = list(map(int,dst_params))
    i = 0
    while i < len(src_params):
        src_param_list.append([src_params[i],src_params[i+1]])
        i +=2
    
    j = 0
    while j < len(dst_params):
        dst_param_list.append([dst_params[j],dst_params[j+1]])
        j +=2

    # print(src_param_list)
    # print(dst_param_list)


    # sourcePoints = np.float32([[50, 50], [200, 50], [50, 200]])
    sourcePoints = np.float32(src_param_list)
    # destPoints = np.float32([[10, 100], [200, 50], [100, 250]])
    destPoints = np.float32(dst_param_list)

    transformedImage = affineTransformationService(image, sourcePoints, destPoints)

    output_image_name = 'Transformation/Output_Images/'+inputImageName
    cv2.imwrite(output_image_name, transformedImage)

    with open(output_image_name, "rb") as image_file:
        image_string = base64.b64encode(image_file.read())
        return image_string


if __name__ == "__main__":
    affineTransformation()
