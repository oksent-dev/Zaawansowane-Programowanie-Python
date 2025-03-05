"""
3. Znajdowanie środka obrazu
a. Wczytaj obraz i oblicz współrzędne jego środka.
b. Pobierz wartość koloru piksela w tym miejscu i wyświetl ją w konsoli.
"""

import cv2

print("Loading image...")
image = cv2.imread("example.jpg")

if image is None:
    print("Error: Can't load image.")
    exit(0)

(height, width, _) = image.shape

center = (width // 2, height // 2)
(b, g, r) = image[center[1], center[0]]
print("Center of the image - Red: {}, Green: {}, Blue: {}".format(r, g, b))
