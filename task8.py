"""
8. Modyfikacja całego wiersza pikseli
a. Wczytaj obraz i zmień kolor wszystkich pikseli w 100. wierszu na zielony
(0, 255, 0) .
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

image[100] = [0, 255, 0]

cv2.namedWindow("Modified", cv2.WINDOW_NORMAL)
cv2.imshow("Modified", image)

cv2.waitKey(0)
cv2.destroyAllWindows()
