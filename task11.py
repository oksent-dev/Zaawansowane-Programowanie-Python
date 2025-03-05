"""
11. Znajdowanie najjaśniejszego piksela w obrazie
a. Przeszukaj cały obraz i znajdź piksel o najwyższej wartości jasności.
b. Wyświetl jego współrzędne i wartość.
"""

import cv2

print("Loading image...")
image = cv2.imread("example.jpg")

if image is None:
    print("Error: Can't load image.")
    exit(0)

max_brightness = 0
max_pixel = None

for y in range(image.shape[0]):
    for x in range(image.shape[1]):
        pixel = image[y, x]
        brightness = int(pixel[0]) + int(pixel[1]) + int(pixel[2])
        if brightness > max_brightness:
            max_brightness = brightness
            max_pixel = (x, y)

print("Brightest pixel: ", max_pixel)
(b, g, r) = image[max_pixel[1], max_pixel[0]]
print(f"R: {r}, G: {g}, B: {b}")
