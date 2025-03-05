"""
5. Kolorowanie fragmentu obrazu
a. Podziel obraz na 4 równe części (ćwiartki).
b. Wypełnij lewą górną ćwiartkę kolorem niebieskim (255, 0, 0) .
c. Wyświetl obraz po zmianach.
"""

import cv2

print("Loading image...")
image = cv2.imread("example.jpg")

if image is None:
    print("Error: Can't load image.")
    exit(0)

(height, width, _) = image.shape

image[0 : height // 2, 0 : width // 2] = [255, 0, 0]

cv2.namedWindow("Image", cv2.WINDOW_NORMAL)
cv2.imshow("Image", image)

cv2.waitKey(0)
cv2.destroyAllWindows()
