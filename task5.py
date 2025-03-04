"""
Otwórz dwa obrazy jednocześnie w osobnych oknach. Upewnij się, że można je zamknąć niezależnie.
"""

import cv2

print("Wczytywanie obrazów...")
image1 = cv2.imread("example.jpg")
if image1 is None:
    print("Błąd: nie można wczytać obrazu!")
    exit()

image2 = cv2.imread("example.jpg")
if image2 is None:
    print("Błąd: nie można wczytać obrazu!")
    exit()

cv2.imshow("Image 1", image1)
cv2.imshow("Image 2", image2)

cv2.waitKey(0)
cv2.destroyAllWindows()
