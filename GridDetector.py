import cv2
import numpy as np


# First step : Using Canny'edges detector and lines using Hough transform

def detectSudoku(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred_frame_gray = cv2.blur(gray, (3, 3))
    edges = cv2.Canny(blurred_frame_gray, 50, 150)

    # edges = cv2.Canny(gray, 50, 150)
    line_image = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
    lines = cv2.HoughLines(edges, 2, np.pi / 180, 250, 0, 0)
    if lines is not None:
        for line in lines:
            for rho, theta in line:
                a = np.cos(theta)
                b = np.sin(theta)
                x0 = a * rho
                y0 = b * rho
                x1 = int(x0 + 1000 * (-b))
                y1 = int(y0 + 1000 * (a))
                x2 = int(x0 - 1000 * (-b))
                y2 = int(y0 - 1000 * (a))

                cv2.line(line_image, (x1, y1), (x2, y2), (0, 0, 255))

    return line_image
