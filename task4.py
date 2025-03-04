"""
4. Wczytaj obraz w skali szarości i zapisz go jako nowy plik - znajdź w dokumentacji odpowiednią funkcję do tego.
"""

import cv2

print("Wczytywanie obrazu...")
image = cv2.imread("example.jpg", cv2.IMREAD_GRAYSCALE)

if image is None:
    print("Błąd: nie można wczytać obrazu!")
    exit()

cv2.imwrite("example_gray.jpg", image)
print("Obraz zapisano jako example_gray.jpg.")
