"""
2. Modyfikacja pojedynczego piksela
a. Zmień kolor piksela w prawym dolnym rogu obrazu na czerwony (0, 0, 255) .
b. Wyświetl obraz przed i po zmianie.
"""

import cv2
import numpy as np

print("Loading image...")
image = cv2.imread("example.jpg")

if image is None:
    print("Error: Can't load image.")
    exit(0)

cv2.namedWindow("Original", cv2.WINDOW_NORMAL)
cv2.imshow("Original", image)

cv2.waitKey(0)

image[-1, -1] = (0, 0, 255)

cv2.namedWindow("Modified", cv2.WINDOW_NORMAL)
cv2.imshow("Modified", image)

cv2.waitKey(0)
cv2.destroyAllWindows()
