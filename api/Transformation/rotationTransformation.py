import numpy as np
import cv2
import base64
import math

def rotate(image, theta):
    [h, w,_] = image.shape
    m = np.array([[math.cos(theta), -math.sin(theta)], [math.sin(theta), math.cos(theta)]])
    m1 = np.array([[math.cos(theta), math.sin(theta)], [-math.sin(theta), math.cos(theta)]])
    l = np.array([h, 0])
    c = np.array([h, w])
    r = np.array([0, w])
    l1 = m.dot(l)
    c1 = m.dot(c)
    r1 = m.dot(r)
    r_origin = np.array([0, 0])
    min_x_val = min(l1[0], c1[0], r1[0], r_origin[0])
    min_y_val = min(l1[1], c1[1], r1[1], r_origin[1])
    max_x_val = max(l1[0], c1[0], r1[0], r_origin[0])
    max_y_val = max(l1[1], c1[1], r1[1], r_origin[1])
    rows = int(max_x_val - min_x_val)
    cols = int(max_y_val - min_y_val)
    [x1, y1] = [-min_x_val, -min_y_val]
    img1 = np.zeros((rows, cols,3))
    for row in range(rows):
        for col in range(cols):
            i1 = row - x1
            j1 = col - y1
            img = np.array([i1, j1])
            [ix, iy] = m1.dot(img)
            # nearest_neighbor interpolation
            ix1 = int(ix)
            iy1 = int(iy)
            if h > ix >= 0 and w > iy >= 0:
                img1[row, col] = image[ix1, iy1]
    return img1

def rotationTransformation(inputImageName,parameters):
    image = cv2.imread('Transformation/Input_Images/'+inputImageName, cv2.IMREAD_COLOR)

    theta = float(parameters)
    rotated_image = rotate(image, theta)

    output_image_name = 'Transformation/Output_Images/'+inputImageName
    cv2.imwrite(output_image_name, rotated_image)

    with open(output_image_name, "rb") as image_file:
        image_string = base64.b64encode(image_file.read())
        return image_string

if __name__ == "__main__": 
    rotationTransformation("Dog.jpg","0.5")