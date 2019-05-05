#######################
# zoomandenhance.py
# Part of homework 5, problem 1
# This function takes a File Image and zooms, resizes and enhances a specific section.
# Input:File Image, and Scaling Factor
# Return: Original Image and new zoomed, resized and enhanced image, in separate windows.
#######################



import cImage
import sys

def zoom(image, upperLeftX, upperLeftY, lowerRightX, lowerRightY, scalingFactor):
    """Zooms the fileImage to the selected portion of the original image and makes the zoomed portion a scalingFactor bigger""" 
    zoom=cImage.EmptyImage(scalingFactor*(lowerRightX+1-upperLeftX),scalingFactor*(lowerRightY+1-upperLeftY))

    for x in range(upperLeftX,lowerRightX+1):
        for y in range(upperLeftY,lowerRightY+1):
            p=image.getPixel(x,y)
            for i in range(scalingFactor):
                for j in range(scalingFactor):
                    zoom.setPixel(scalingFactor*(x-upperLeftX)+i,scalingFactor*(y-upperLeftY)+j,p)
    return zoom

def restrict(num, minNum, maxNum):
    """Takes the number and makes restrics it to a minimum and maxiumum number."""
    if num>=minNum and num<=maxNum:
        num=num
    elif num < minNum:
        num=minNum
    else:
        num=maxNum

    return num

def sharpenImage(image):
    """Takes the image provided on the command-line and makes each pixel "less like those around it" in order for them to pop-out better"""
    enhanced= cImage.EmptyImage(image.getWidth(), image.getHeight())
    
    for x in range(image.getWidth()):
        for y in range(image.getHeight()):
            p=image.getPixel(x,y)
            if x==0 or x==image.getWidth()-1:
                enhanced.setPixel(x,y,p)
            elif y==0 or y==image.getHeight()-1:
                enhanced.setPixel(x,y,p)
            else:
                r=10*p.getRed()
                g=10*p.getGreen()
                b=10*p.getBlue()
                for i in range(3):
                    for j in range(3):
                        p=image.getPixel(x+i-1,y+j-1)
                        r=r-p.getRed()
                        g=g-p.getGreen()
                        b=b-p.getBlue()
                r =restrict(r,0,255)
                g =restrict(g,0,255)
                b =restrict(b,0,255)
                enhancedP=cImage.Pixel(r ,g ,b )
                enhanced.setPixel(x,y,enhancedP)
    return enhanced

def main():
   
    """Takes an image filename as a command line argument. The function allows the user to select a region to zoom in on using the mouse as well as to specify a scaling factor. The region is "Zoomed...and Enhanced!" and displayed on the screen."""
    filename = sys.argv[1]

    #Create two copies of the given image
    #One that we will draw a green box on
    image = cImage.FileImage(filename)
    #The other we will pass to the processing functions
    imageCopy = cImage.FileImage(filename)

    #Display the given image
    originalWin = cImage.ImageWin("Original", image.getWidth(), image.getHeight())
    image.draw(originalWin)

    #Keeps asking the user to pick a region to zoom in on
    #until they make a valid choice
    picked = False
    while not picked:
        print("Please click the upper-left corner of the region")
        upperLeft = originalWin.getMouse()
        print("Please click the lower-right corner of the region")
        lowerRight = originalWin.getMouse()
        
        if lowerRight[0] < upperLeft[0] or lowerRight[1] < upperLeft[1]:
            print("Not a valid region")
        else:
            picked = True

    #Have to adjust the coordinates in the windw to account 
    #for the white border created by cImage
    ulX = upperLeft[0] - 5
    ulY = upperLeft[1] - 5
    lrX = lowerRight[0] - 5
    lrY = lowerRight[1] - 5

    #Create a green pixel for drawing a box around the zoom region.
    boxPixel = cImage.Pixel(0, 255, 0)

    #Draw the top and bottom sides of the box
    for x in range(ulX, lrX + 1):
        if ulY > 0:
            image.setPixel(x, ulY - 1, boxPixel)
            
        if lrY < image.getHeight() - 1:
            image.setPixel(x, lrY + 1, boxPixel)

    #Draw the left and right sides of the box
    for y in range(ulY, lrY + 1):
        if ulX > 0:
            image.setPixel(ulX - 1, y, boxPixel)

        if lrX < image.getWidth() - 1:
            image.setPixel(lrX + 1, y, boxPixel)

    #Keeps asking the user for a scaling factor
    #until they input something that is at least 1.
    scale = 0
    while scale <= 0:
        scale = int(input("Please pick a scaling factor (at least 1): "))

    print("Zooming and Enhancing...")
    
    #Sharpen the image ("enhance")
    enhanced = sharpenImage(imageCopy)
    
    #Zoom in on the specified region
    zoomed = zoom(enhanced, ulX, ulY, lrX, lrY, scale)

    #Display the enhanced and zoomed image
    zoomWin = cImage.ImageWin("Zoom...and Enhance!", zoomed.getWidth(), zoomed.getHeight())
    zoomed.draw(zoomWin)

    print("Click the zoom window to exit, when ready.")
    zoomWin.exitOnClick()

main()
    

