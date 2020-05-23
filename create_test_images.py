import os
import cv2
import numpy as np
from skimage import io

parent = os.listdir("C:/Users/LR/Desktop/DL_video_frames/test")

x = []
y = []
count = 0
output = 0

for video_class in parent[1:]:  # it also contains DS.store file
    child = os.listdir("C:/Users/LR/Desktop/DL_video_frames/test/" + video_class)
    for class_i in child[1:]:
        sub_child = os.listdir("C:/Users/LR/Desktop/DL_video_frames/test/" + video_class + "/" + class_i)
        for image_fol in sub_child[1:]:
            print(image_fol)
            if video_class == 'class_4':
                if count % 4 == 0:  # (selected images at gap of 4)
                    image = io.imread("C:/Users/LR/Desktop/DL_video_frames/test/" + video_class + "/" + class_i + "/" + image_fol)
                    x.append(image)
                    y.append(output)
                    cv2.imwrite('C:/Users/LR/Desktop/DL_project_videos/validate/' + video_class + '/' + str(count) + '_' + image_fol, image)
                count += 1

            else:
                if count % 8 == 0:
                    image = io.imread("C:/Users/LR/Desktop/DL_video_frames/test/" + video_class + "/" + class_i + "/" + image_fol)
                    x.append(image)
                    y.append(output)
                    cv2.imwrite('C:/Users/LR/Desktop/DL_video_frames/validate/' + video_class + '/' + str(count) + '_' + image_fol, image)
                count += 1
    output += 1
x = np.array(x)
y = np.array(y)
print("x", len(x), "y", len(y))
