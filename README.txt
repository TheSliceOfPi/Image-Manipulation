# Image-Manipulation
Crop and Zoom into an image using CImage on Python,

The zoomandenhance module takes four functions: zoom, restrict, sharpenImage, and main. The zoom function take a FileImage whose name was provided by the user on the command-line and zooms into the area selected by the user, and increases the size of the section by a scaling factor, provided by the user on the command-line. 
The restrict function takes the pixel value and then determines if the number fits within the desired range (0 to 255). If the number does not fit within the range then the number has to be increased to the minimum number or decreased to the maximum number. 
The sharpenImage function takes a FileImage whose name was provided by the user on the command-line and “sharpens” the image, or makes the image less like the surrounding pixels.
 In order to do this, the function has to take a pixel, multiply it the pixel value by the total number of pixels (nine), subtracts the pixel value of each pixel to the multiplication. SharpenImage then calls restrict to make sure the pixel values are within the range 0 and 255, and replaces the original pixel value by this new value. 
The main function takes the FileImage whose name was provided by the user on the command-line and makes two copies, an original and one that will be processed. 
Main then asks the user for the specific area they want to “Zoom and Enhance” and the desired scaling Factor. 
Main then calls sharpenImage, to sharpen the image. Main then calls zoom, to zoom into the desired image section and increase the image size by the scale provided by the user. Main then draws both original image and the new enhanced, zoomed, and rescaled image onto an image window. 

#Run: python3 zoomandenhance.py <Name of File Image> 
