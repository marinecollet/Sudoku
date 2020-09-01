import cv2
import numpy as np
import GridDetector

# Displaying the camera in realtime
cap = cv2.VideoCapture(0)

while (True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    #Adding feature on the image to detect the Sudoku
    canny = GridDetector.detectSudoku(frame)
    GridDetector.detectSudoku(frame)

    # Display the resulting frame
    cv2.imshow('frame', canny)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


