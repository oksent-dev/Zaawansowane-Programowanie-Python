"""
6. Wypełnienie konkretnego obszaru obrazu jednolitym kolorem
Pobierz współrzędne środka obrazu.
Wypełnij kwadrat o wymiarach 100x100 px, którego środek pokrywa się ze środkiem obrazu, kolorem czerwonym (0, 0, 255) .
Wyświetl obraz po zmianach.
"""

import cv2

print("Loading image...")
image = cv2.imread("example.jpg")

if image is None:
    print("Error: Can't load image.")
    exit(0)

(height, width, _) = image.shape

center = (width // 2, height // 2)
size = 100

image[
    center[1] - size // 2 : center[1] + size // 2,
    center[0] - size // 2 : center[0] + size // 2,
] = [0, 0, 255]

cv2.namedWindow("Image", cv2.WINDOW_NORMAL)
cv2.imshow("Image", image)

cv2.waitKey(0)
cv2.destroyAllWindows()
