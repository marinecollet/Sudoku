import cv2

imgsrc = "C:\\Users\\Admin\\Pictures\\a.png"

img = cv2.imread(imgsrc, 0)
res = cv2.resize(img, (600, 600))
cv2.imshow('image', res)
cv2.waitKey(0)
cv2.destroyAllWindows()


