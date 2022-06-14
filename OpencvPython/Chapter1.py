import cv2

print("Package Imported")

img = cv2.imread("Resources/eillish.jpg")

cv2.imshow("Output", img)
cv2.waitKey(1000)
