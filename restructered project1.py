#CST205
#Jason Kirn
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

pictures = [im1, im2, im3, im4, im5, im6, im7, im8, im9]
newIm = Image.new("RGB", (495, 557))
red = [1, 2, 3, 4, 5, 6, 7, 8, 9]
green = [1, 2, 3, 4, 5, 6, 7, 8, 9]
blue = [1, 2, 3, 4, 5, 6, 7, 8, 9]

#redCounter = 0

def getRforImage():
    global redCounter
    global pixelCount
    pixelCount = 1
    #imRed = Image.new("RGB", (495, 557))
    for x in range(495):
        for y in range(557):
            redCounter = 0
            while (redCounter < 9):
                red[redCounter], green[redCounter], blue[redCounter] = pictures[redCounter].getpixel((x,y))
                #imRed.putpixel((x,y),pix[0]) # [0 is the first tuple item] aka red
                #red[redCounter] =
                #print ("\nImage number " + str(redCounter + 1) + " Progress: " + str(pixelCount) + " of " + str(275715) + "pixels...")
                pixelCount = pixelCount + 1
    #red[redCounter] = imRed
                redCounter = redCounter + 1
            #median:
            sortedRed = sorted(red)
            sortedGreen = sorted(green)
            sortedBlue = sorted(blue)
            newIm.putpixel((x,y),(sortedRed[4],sortedGreen[4],sortedBlue[4]))
            #print (red[redCounter])




def getGforImage():
    global greenCounter
    global pixelCount2
    pixelCount2 = 1
    imGreen = Image.new("RGB", (495, 557))
    for x in range(495):
        for y in range(557):
            pix = pictures[greenCounter].getpixel((x,y))
            imGreen.putpixel((x,y),pix[1])
            print ("\nImage number " + str(greenCounter + 1) + " Progress: " + str(pixelCount2) + " of " + str(275715) + "pixels...")
            pixelCount2 = pixelCount2 + 1
    green[greenCounter] = imGreen
    greenCounter = greenCounter + 1

def getBforImage():
    global blueCounter
    global pixelCount3
    pixelCount3 = 1
    imBlue = Image.new("RGB", (495, 557))
    for x in range(495):
        for y in range(557):
            pix = pictures[blueCounter].getpixel((x,y))
            imBlue.putpixel((x,y),pix[2])
            print ("\nImage number " + str(blueCounter + 1) + " Progress: " + str(pixelCount3) + " of " + str(275715) + "pixels...")
            pixelCount3 = pixelCount3 + 1
    blue[blueCounter] = imBlue
    blueCounter = blueCounter + 1
#for loop: #goal: call the function
#for x in range (9):
getRforImage()

#newIm.save()
newIm.show()
    #input()
    #getGforImage()
    #gerBforImage()
    #red[redCounter - 1].show()#don't need this in the end product
#median odd, cuz 9 images
