import os
import math
import cv2

parent = os.listdir("C:/Users/LR/Desktop/DL_project_videos/")

for video_class in parent[1:]:
    print(video_class)
    listing = os.listdir("C:/Users/LR/Desktop/DL_project_videos/"+video_class)
    count = 1
    for file in listing:
        video = cv2.VideoCapture("C:/Users/LR/Desktop/DL_project_videos/" + video_class + "/" + file)
        frameId = video.get(1)
        print(video.isOpened())
        framerate = video.get(5)
        os.makedirs("C:/Users/LR/Desktop/DL_video_frames/" + video_class+"/" + "video_" + str(int(count)))
        while video.isOpened():
            success, image = video.read()
            if success != True:
                break
            frame_count = 1
            while success:
                image = cv2.resize(image, (224, 224), interpolation=cv2.INTER_AREA)
                cv2.imwrite("C:/Users/LR/Desktop/DL_video_frames/" + video_class + "/" + "video_" + str(
                    int(count)) + "/image_%d.jpg" % frame_count, image)  # save frame as JPEG file
                success, image = video.read()
                print('Read a new frame: ', success)
                frame_count += 1
        video.release()
        print('done')
        count += 1
