from PIL import Image

img = Image.open('image.png').convert('RGB')
width, height = img.size

msg = "I am Noah Vendrig"
bin_msg = [''.join(format(ord(letter), '08b')) for letter in msg] # convert each char to binary in a string

print(bin_msg)

curr_pixel = 1
for num in bin_msg:
    for digit in num:
        digit = int(digit)
        r,g,b = img.getpixel((curr_pixel, curr_pixel))
        img.putpixel((curr_pixel,curr_pixel),(digit, g, b))
        curr_pixel += 10
    curr_pixel += 10

img.show()
img.save("encoded.png")