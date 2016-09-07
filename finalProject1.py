#CST205
#Jason Kirn
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

pictures = [im1, im2, im3, im4, im5, im6, im7, im8, im9]#Store them into an array

newIm = Image.new("RGB", (495, 557))#create a new blank image to put the result into

red = [1, 2, 3, 4, 5, 6, 7, 8, 9]#Arrays to hold the r, g, b pixels
green = [1, 2, 3, 4, 5, 6, 7, 8, 9]
blue = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def getImagesPixelMedian():
    for x in range(495):
        for y in range(557):
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
