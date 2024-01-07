import cv2
import numpy as np

# Video is a series of images (frames) played in a sequence
# The following line will open the webcam of the computer
video = cv2.VideoCapture(0)

while True:
    # status is a boolean value that tells us if the video is still running or not
    status, frame = video.read()
    if not status:
        break

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    inverted_frame = frame * 255
    # To invert the gray frame, we will multiply it by 255
    inverted_gray_frame = gray_frame * 255
    
    # if the video is still running, we will show the frame
    cv2.imshow('Video', frame)
    cv2.imshow('Inverted Video', inverted_frame)
    cv2.imshow('Gray Video', gray_frame)
    cv2.imshow('Gray Inverted Video', inverted_gray_frame)

    # if the user presses the escape key, we will break the loop
    if cv2.waitKey(1) == 27:
        break
# This is done to release the video from the memory
video.release()

# This is done to destroy all the windows that were created
cv2.destroyAllWindows()