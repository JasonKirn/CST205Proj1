from PIL import Image
im1 = Image.open("1.PNG")
im2 = Image.open("2.PNG")
im3 = Image.open("3.PNG")
im4 = Image.open("4.PNG")
im5 = Image.open("5.PNG")
im6 = Image.open("6.PNG")
im7 = Image.open("7.PNG")
im8 = Image.open("8.PNG")
im9 = Image.open("9.PNG")
rgb_im1 = im1.convert('RGB')
rgb_im2 = im2.convert('RGB')
rgb_im3 = im3.convert('RGB')
rgb_im4 = im4.convert('RGB')
rgb_im5 = im5.convert('RGB')
rgb_im6 = im6.convert('RGB')
rgb_im7 = im7.convert('RGB')
rgb_im8 = im8.convert('RGB')
rgb_im9 = im9.convert('RGB')

pictures = [rgb_im1, rgb_im2, rgb_im3, rgb_im4, rgb_im5,
 rgb_im6, rgb_im7, rgb_im8, rgb_im9 ]

for pictures

pix1 = rgb_im1.getpixel((0,0))



print (pix1)

print (im1.size)
