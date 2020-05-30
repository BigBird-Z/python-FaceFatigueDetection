import cv2 as cv

import numpy as np


def video_demo():
    capture = cv.VideoCapture(0)
    # 捕获摄像头 用数字控制不同的设备，视频文件指定好路径
    while(True):
        ret, frame = capture.read()
        cv.imshow("video", frame)
        c = cv.waitKey(50)
        if c == 27:
            break

def get_image_info(image):
    print(type(image))
    print(image.dtype)
    print(image.shape)
    print(image.size)


src = cv.imread("F:/pythonProgram/projectFile/image/01.jpg")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)
video_demo()

get_image_info(src)
cv.waitKey(0)
cv.destroyAllWindows()
