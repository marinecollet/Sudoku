import cv2
import numpy as np
import math


# First step : Using Canny'edges detector and lines using Hough transform

def detectSudoku(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred_frame_gray = cv2.blur(gray, (3, 3))
    edges = cv2.Canny(blurred_frame_gray, 50, 150)

    # edges = cv2.Canny(gray, 50, 150)
    line_image = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
    lines = cv2.HoughLines(edges, 2, np.pi / 180, 250, 0, 0)

    vertical_lines = []
    horizontal_lines = []

    if lines is not None:
        for line in lines:
            for rho, theta in line:
                # if theta is greater than 180, rho become negative and theta do not rises but decreases
                a = np.cos(theta)
                b = np.sin(theta)
                x0 = a * rho
                y0 = b * rho
                x1 = int(x0 + 1000 * (-b))
                y1 = int(y0 + 1000 * (a))
                x2 = int(x0 - 1000 * (-b))
                y2 = int(y0 - 1000 * (a))
                if 135 > math.degrees(theta) > 45:  # horizontal lines between 45 and 90 + 45 degrees
                    cv2.line(line_image, (x1, y1), (x2, y2), (0, 0, 255))
                    horizontal_lines.append(getFunction((x1, y1), (x2, y2)))
                else:  # vertical lines
                    cv2.line(line_image, (x1, y1), (x2, y2), (0, 255, 0))
                    vertical_lines.append(getFunction((x1, y1), (x2, y2)))
                if len(vertical_lines) != 0 and len(horizontal_lines) != 0:
                    for i in range(0, len(vertical_lines)):
                        for j in range(0, len(horizontal_lines)):
                            (x, y) = intersection(vertical_lines[i], horizontal_lines[j])
                            cv2.circle(line_image, (int(x), int(y)), 2, (255, 0, 0), 2)
    return line_image


# droite A depuis a1, a2 : A = coeffa * x + Ka
# droite B depuis b1, b2 : B = coeffb * x + Kb
def intersection(a, b):
    coeffa = a[0]
    Ka = a[1]
    coeffb = b[0]
    Kb = b[1]

    xIntersect = (Ka - Kb) / (coeffb - coeffa)
    YIntersect = coeffa * xIntersect + Ka
    return (xIntersect, YIntersect)


# f(x) = coeffa * x + Ka
def getFunction(a1, a2):
    if (a2[0] == a1[0]):
        coeffa = 0
        Ka = a1[1]
    else:
        coeffa = ((a2[1] - a1[1]) / (a2[0] - a1[0]))
        Ka = a1[1] - (coeffa) * a1[0]
    return (coeffa, Ka)
