"""
1. Odczyt wartości piksela
a. Wczytaj obraz i pobierz wartość piksela znajdującego się w lewym górnym rogu (współrzędne 0,0 ).
b. Wyświetl wartości składowych koloru (R, G, B).
"""

import cv2

print("Loading image...")
image = cv2.imread("example.jpg")

if image is None:
    print("Error: Can't load image.")
    exit(0)

(b, g, r) = image[0, 0]
print("Pixel at (0, 0) - Red: {}, Green: {}, Blue: {}".format(r, g, b))
