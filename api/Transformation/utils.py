import numpy as np
from matplotlib import pyplot as plt


def plotImg(img):
    img = img.astype(np.uint8)
    plt.imshow(img)
    plt.show()


def convertAsMatrix(img):
    row, col, channel = img.shape
    matrix = np.zeros((col, row, channel), dtype='int')
    for i in range(img.shape[0]):
        matrix[:, i] = img[i]
    return matrix


def convertAsImg(mtr):
    col, row, channel = mtr.shape
    img = np.zeros((row, col, channel), dtype='int')
    for i in range(mtr.shape[0]):
        img[:, i] = mtr[i]

    return img
