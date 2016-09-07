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
rgb_im1 = im1.convert('RGB')#don't need probably
rgb_im2 = im2.convert('RGB')
rgb_im3 = im3.convert('RGB')
rgb_im4 = im4.convert('RGB')
rgb_im5 = im5.convert('RGB')
rgb_im6 = im6.convert('RGB')
rgb_im7 = im7.convert('RGB')
rgb_im8 = im8.convert('RGB')
rgb_im9 = im9.convert('RGB')

pictures = [rgb_im1, rgb_im2, rgb_im3, rgb_im4, rgb_im5,
 rgb_im6, rgb_im7, rgb_im8, rgb_im9]

red = [1, 2, 3, 4, 5, 6, 7, 8, 9]#just to initialize
green = [1, 2, 3, 4, 5, 6, 7, 8, 9]
blue = [1, 2, 3, 4, 5, 6, 7, 8, 9]

pixelCount = 1

for x in range (495):#all the x values.  495 or 494
    for y in range (557):#all the y values
        counter = 0
        for picture in pictures:
            pix = picture.getpixel((x,y))
            #print("pix[0] is:")
            #print(pix[0])
            imRed = Image.new("RGB", (495, 557))
            imGreen = Image.new("RGB", (495, 557))
            imBlue = Image.new("RGB", (495, 557))
            #print("imRed is:")
            #print(imRed)
            #red[counter] = imRed
            #print("Red's current Counter is at:")
            #print(str(counter))
            #print(red[counter])
            #input()
            imRed.putpixel((x,y),red[counter])#[] or ()
            imGreen.putpixel((x,y),green[counter])
            imBlue.putpixel((x,y),blue[counter])
            #pix[1]
            #pix[2]
            #imRed.save("hibgib.RGB")
            print("\nProgress: " + str(pixelCount) + "of" + str(275715) + "pixels...")
            pixelCount = pixelCount + 1
            #input()
            counter = counter + 1#used for the red blue gren. Store using putpixel red in all reds.
            #ex. red[1] has all red pixels of image 1


            '''pix = picture.getpixel((x,y))
            imRed = Image.new("RGB", (495, 557))
            red[counter] = imRed
            print("blah")

            #pix[0] = imRed.putpixel((x,y),red[x,y])#[] or ()
            #pix[1]
            #pix[2]
            print(pix)
            print(imRed)
            print(red[counter])
            counter = counter + 1#used for the red blue gren. Store using putpixel red in all reds.
            #ex. red[1] has all red pixels of image 1
pixTest = picture.getpixel((0,0))
pixTest2 = picture.getpixel((300,234))'''
imRed.show()
imGreen.show()
imBlue.show()

'''print(pixTest2)
print(pixTest2[0])#red pixel
print(pixTest2[1])#blue pixel
print(pixTest2[2])#green pixel
print(pixTest[0])
print("Content of red: ")
print(red[0])'''



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


#pix1 = rgb_im1.getpixel((0,0))



#print (pix1)

#print (im1.size)
