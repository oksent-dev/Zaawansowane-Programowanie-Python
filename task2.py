"""
2. Wczytaj zdjęcie w kolorze i wyświetl liczbę kanałów.
"""

import cv2

print("Wczytywanie obrazu...")
image = cv2.imread("example.jpg")

if image is None:
    print("Błąd: nie można wczytać obrazu!")
    exit()

(h, w, c) = image.shape[:3]
print(f"width: {w} pixels")
print(f"height: {h} pixels")
print(f"channels: {c}")
