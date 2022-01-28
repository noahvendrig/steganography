from PIL import Image

img = Image.open('encoded.png').convert('RGB')
width, height = img.size

curr_pixel = 1
decoding = True

bin_msg = []
curr_num = ''
while decoding:
    
    r,g,b = img.getpixel((curr_pixel, curr_pixel))
    if r == 0 or r == 1: # only works if there is actually a message (the image is not blank)
        curr_num += str(r)
        curr_pixel += 10
    else:
        curr_pixel += 10
        if r == 0 or r == 1:
            curr_num += str(r)
            curr_pixel += 10
        else: 
            bin_msg.append(curr_num)

print(bin_msg)

