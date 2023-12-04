import cv2
import os
import numpy as np
from skimage import io


def read_path(file_pathname1, file_pathname2):

    for filename1 in os.listdir(file_pathname1):

        for filename2 in os.listdir(file_pathname2):
            if filename1 == filename2:
                img1 = cv2.imread(file_pathname1 + '/' + filename1)
                img2 = cv2.imread(file_pathname2 + '/' + filename2)
                print(img1.shape)  #
                rows = img1.shape[0]
                cols = img1.shape[1]
                img = np.zeros((rows, cols, 3), dtype=img1.dtype)
                for row in range(rows):
                    for col in range(cols):
                        if np.any(img2[row, col] != 0):
                            img[row, col] = img2[row, col]
                        else:
                            img[row, col] = img1[row, col]

                image_np = np.hstack((img1, img))

                cv2.imwrite('\\result' + "/" + filename1,
                            image_np)


