"""
10. Sprawdzenie różnicy wartości pikseli
a. Pobierz wartości pikseli w dwóch różnych miejscach obrazu i porównaj je
(np. (50,50) i (200,200) ).
b. Wypisz różnice w wartościach R, G, B.
"""

import cv2

print("Loading image...")
image = cv2.imread("example.jpg")

if image is None:
    print("Error: Can't load image.")
    exit(0)

pixel1 = image[50, 50]
pixel2 = image[200, 200]

(b, g, r) = pixel1 - pixel2

print("Difference in R: ", r)
print("Difference in G: ", g)
print("Difference in B: ", b)
