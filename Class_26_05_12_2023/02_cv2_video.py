import cv2
import numpy as np

# Video is a series of images (frames) played in a sequence
video = cv2.VideoCapture('Class_26_05_12_2023/video.mp4')

while True:
    # status is a boolean value that tells us if the video is still running or not
    status, frame = video.read()

    if not status:
        break
    
    ###########################################################
    ###### Here we will do some processing on the frame #######
    ###########################################################

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    ###########################################################

    # if the video is still running, we will show the frame
    cv2.imshow('Video', frame)
    cv2.imshow('Gray Video', gray_frame)

    # if the user presses the escape key, we will break the loop
    if cv2.waitKey(1) == 27:
        break

# This is done to release the video from the memory
video.release()

# This is done to destroy all the windows that were created
cv2.destroyAllWindows()