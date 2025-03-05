"""
9. Zmiana wartości pikseli w określonym zakresie
a. Wypełnij obszar od (50,50) do (100,100) kolorem białym (255, 255, 255) .
b. Wyświetl obraz przed i po zmianie.
"""

import cv2

print("Loading image...")
image = cv2.imread("example.jpg")

if image is None:
    print("Error: Can't load image.")
    exit(0)

cv2.namedWindow("Image", cv2.WINDOW_NORMAL)
cv2.imshow("Image", image)

cv2.waitKey(0)
cv2.destroyAllWindows()

image[50:101, 50:101] = [255, 255, 255]

cv2.namedWindow("Modified", cv2.WINDOW_NORMAL)
cv2.imshow("Modified", image)

cv2.waitKey(0)
cv2.destroyAllWindows()
