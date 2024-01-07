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

    # If we want to create a rectangle on the frame, we will use the following line
    cv2.rectangle(frame, (100, 100), (300, 300), (0, 0, 255), 5)
    # For circle we will use the following line
    cv2.circle(frame, (400, 400), 50, (0, 255, 0), 5)
    # To add text, we can use the putText function
    cv2.putText(frame, 'Hello World', (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 2)

    cv2.imshow('Video', frame)

    # if the user presses the escape key, we will break the loop
    if cv2.waitKey(1) == 27:
        break
# This is done to release the video from the memory
video.release()

# This is done to destroy all the windows that were created
cv2.destroyAllWindows()