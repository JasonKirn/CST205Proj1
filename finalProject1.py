#CST205
#Jason Kirn
#https://github.com/JasonKirn/CST205Proj1/blob/master/finalProject1.py
from PIL import Image
im1 = Image.open("1.PNG")#Start by opening all the given images
im2 = Image.open("2.PNG")
im3 = Image.open("3.PNG")
im4 = Image.open("4.PNG")
im5 = Image.open("5.PNG")
im6 = Image.open("6.PNG")
im7 = Image.open("7.PNG")
im8 = Image.open("8.PNG")
im9 = Image.open("9.PNG")
rgb_im1 = im1.convert('RGB')#This is not needed for this project, however
rgb_im2 = im2.convert('RGB')#if you download images online you may need this
rgb_im3 = im3.convert('RGB')#to convert RGBA format to RGB so that this program's
rgb_im4 = im4.convert('RGB')#use of getpixel always works with any pictures.
rgb_im5 = im5.convert('RGB')
rgb_im6 = im6.convert('RGB')
rgb_im7 = im7.convert('RGB')
rgb_im8 = im8.convert('RGB')
rgb_im9 = im9.convert('RGB')

pictures = [rgb_im1, rgb_im2, rgb_im3, rgb_im4, rgb_im5,
 rgb_im6, rgb_im7, rgb_im8, rgb_im9]#Store them into an array

width, height = im1.size#grab size of the images, must be similar sizes.

newIm = Image.new("RGB", (width, height))#create a new blank image to put the result into

red = [1, 2, 3, 4, 5, 6, 7, 8, 9]#Arrays to hold the r, g, b pixels
green = [1, 2, 3, 4, 5, 6, 7, 8, 9]
blue = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def getImagesPixelMedian():
    for x in range(width):
        for y in range(height):
            counter = 0
            while (counter < 9):
                #Get r, g, b pixels from image 1-9, starting at 0 because of indexing
                red[counter], green[counter], blue[counter] = pictures[counter].getpixel((x,y))

                #counter for while loop condition
                counter = counter + 1

            #median:
            sortedRed = sorted(red)
            sortedGreen = sorted(green)
            sortedBlue = sorted(blue)
            newIm.putpixel((x,y),(sortedRed[4],sortedGreen[4],sortedBlue[4]))

#call the function to perform its task
getImagesPixelMedian()

newIm.save("Result.PNG")
newIm.show()
