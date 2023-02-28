from PIL import Image
import numpy as np


# first convert image into array now array this thing can be imagined as a 2d array in which each element array gives the rgb data of that element
# so we select all the r"s the b"s the g's and using a formula i found on the net give each of them a multiplier and form a new 2d array which is a new picture with these alter rgbs
# converting back to jpg


img = Image.open(r"C:\Users\Abhay\Desktop\robocon recruit\Recruitment-22\Image_Processing\Task_1\Grayscale\bees.jpg")

I_array = np.array(img)
print(I_array)

r = I_array[:,:,0]
g = I_array[:,:,1]
b = I_array[:,:,2]

I_gray = r*.299+g*.587+b*.114


im = Image.fromarray(np.uint8(I_gray))
print("--------------------")


im.show()
im.save(r"C:\Users\Abhay\Desktop\robocon recruit\Recruitment-22\Image_Processing\Task_1\Grayscale\gray.jpg")


