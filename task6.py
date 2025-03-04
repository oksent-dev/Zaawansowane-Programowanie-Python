"""
Zmień rozmiar okna wyświetlania obrazu tak, by dostosować je do różnych
ekranów, np. cv2.WINDOW_NORMAL - znajdź w dokumentacji odpowiednią funkcję
do tego.
"""

import cv2


print("Wczytywanie obrazu...")
image = cv2.imread("example.jpg")

if image is None:
    print("Błąd: nie można wczytać obrazu!")
    exit()

cv2.namedWindow("Image", cv2.WINDOW_NORMAL)

cv2.imshow("Image", image)

cv2.waitKey(0)
cv2.destroyAllWindows()
