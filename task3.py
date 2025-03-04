"""
3. Wczytaj zdjęcie w odcieniach szarości i wyświetl liczbę kanałów.
"""

import cv2

print("Wczytywanie obrazu...")
image_gray = cv2.imread("example.jpg", cv2.IMREAD_GRAYSCALE)

if image_gray is None:
    print("Błąd: nie można wczytać obrazu!")
    exit()

(h, w) = image_gray.shape[:2]
print(f"width: {w} pixels")
print(f"height: {h} pixels")
print(
    f"channels: 1"
)  # because shape returns 2 values width and height, so we know that there is only 1 channel
