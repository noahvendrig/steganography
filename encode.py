from PIL import Image

img = Image.open('image.png').convert('RGB')
width, height = img.size  # not in use atm

msg = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem"
bin_msg = [''.join(format(ord(letter), '08b'))
           for letter in msg]  # convert each char to binary in a string

# print(bin_msg)


def encode1(img, bin_msg):
    curr_pixel = 1
    for num in bin_msg:
        for digit in num:
            digit = int(digit)
            r, g, b = img.getpixel((curr_pixel, curr_pixel))
            img.putpixel((curr_pixel, curr_pixel), (digit, g, b))
            curr_pixel += 2
        curr_pixel += 2
    return img


encoded_img = encode1(img, bin_msg)

encoded_img.show()
encoded_img.save("encoded.png")
