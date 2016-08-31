from PIL import Image
im1 = Image.open("1.PNG")

rgb_im1 = im1.convert('RGB')
pix1 = rgb_im1.getpixel((0,0))

print (pix1)

print (im1.size)
