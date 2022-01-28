from PIL import Image

img = Image.open('encoded.png').convert('RGB')
width, height = img.size

curr_pixel = 1
decoding = True

bin_msg = []

while decoding:
    curr_num = ''
    for n in range(8): # each binary string is only 8 digits long
        r,g,b = img.getpixel((curr_pixel, curr_pixel))
        if r == 0 or r == 1:
            curr_num += str(r)
            curr_pixel += 10
        else:
            decoding = False
            # raise ValueError("Invalid pixel value")
            
    bin_msg.append(curr_num)
    curr_pixel += 10

print(bin_msg)
ascii_text = ""
for i in bin_msg[:-1]: # ignore the last empty string in the array
    ascii_text += chr(int(i,2))

print(f"The Message Is: '{ascii_text}'")
