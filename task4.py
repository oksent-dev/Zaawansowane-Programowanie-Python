"""
4. Zamiana wartości piksela na czarny
a. Pobierz od użytkownika współrzędne (x, y) .
b. Stwórz walidację, która zweryfikuje czy podane współrzędne nie
wychodzą poza wymiar zdjęcia.
c. Ustaw piksel w tym miejscu na czarny (0, 0, 0) .
"""

import cv2

print("Loading image...")
image = cv2.imread("example.jpg")

if image is None:
    print("Error: Can't load image.")
    exit(0)

(x, y) = input("Enter coordinates (x, y): ").split()
(x, y) = (int(x), int(y))

(height, width, _) = image.shape

if x < 0 or x >= width or y < 0 or y >= height:
    print("Error: Coordinates out of bounds.")
    exit(0)

image[y, x] = (0, 0, 0)

cv2.namedWindow("Modified", cv2.WINDOW_NORMAL)
cv2.imshow("Modified", image)

cv2.waitKey(0)
cv2.destroyAllWindows()
