import cv2

img = cv2.imread('image.jpg', cv2.IMREAD_UNCHANGED)
height, width, channels = img.shape

msg = "I am Noah"
for letter in msg:
    print(letter)
