"""
7. Wycięcie fragmentu obrazu
a. Podziel obraz na 9 równych części.
b. Pobierz fragment obrazu obejmujący środek.
c. Wyświetl wycięty fragment osobno.
"""

import cv2

print("Loading image...")
image = cv2.imread("example.jpg")

if image is None:
    print("Error: Can't load image.")
    exit(0)

(height, width, _) = image.shape

image = image[height // 3 : 2 * height // 3, width // 3 : 2 * width // 3]

cv2.namedWindow("Image", cv2.WINDOW_NORMAL)
cv2.imshow("Image", image)

cv2.waitKey(0)
cv2.destroyAllWindows()
