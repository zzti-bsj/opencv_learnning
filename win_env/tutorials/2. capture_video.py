# 1. cv.VideoCapture   -->  init capture obj
# 2. cap.isOpened  --> returns the flag that whether the init successful
# 3. cap.read      --> grab, decode and returns next video frame
# 4. cv.cvtColor   --> convert image color
# 5. cap.release   --> closes file or capturing device
# 6. cv.destroyAllWindows  --> destroy all this opened windows

import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open Camera")
    exit()

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # Our operations on the frame come here
    # gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # Display the resulting frame
    cv.imshow('frame', frame)
    if cv.waitKey(1) == ord('q'):
        break
# when everything done, release the capture
cap.release()
cv.destroyAllWindows()