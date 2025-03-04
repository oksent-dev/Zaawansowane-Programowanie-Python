"""
1. Wczytaj i wyświetl obraz z podanej przez siebie ścieżki. Sprawdź, co się stanie, gdy podasz błędną ścieżkę.
"""

import cv2

print("Wczytywanie obrazu...")
image = cv2.imread("example.jpg")

if image is None:
    print("Błąd: nie można wczytać obrazu!")
else:
    print("Obraz wczytano poprawnie.")

print("")
print("Wczytywanie nieistniejącego obrazu...")
non_existing_image = cv2.imread("non_existing.jpg")

if non_existing_image is None:
    print("Błąd: nie można wczytać obrazu!")
else:
    print("Obraz wczytano poprawnie.")
