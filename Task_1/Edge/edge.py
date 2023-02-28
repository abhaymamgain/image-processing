import PIL
from PIL import Image
import numpy as np

# this just basically calculate the magnitude change between rgb values now that in gray scale we have a common rgb value 
# for each cell this filter gives us a magnitude change between sets 2 sets of 3 pixels applied for each direction and assignes
# a value between 0,255 if a large difference is there we get a number closer to 255 if no diff we get close to 0 hence black

img = Image.open(r"C:\Users\Abhay\Desktop\robocon recruit\Recruitment-22\Image_Processing\Task_1\Edge\flower.jpg")

img_arr = np.array(img)

vertical_edges= np.zeros_like(img)

vertical_filter=[[-1,-2,-1],[0,0,0],[1,2,1]]
hori_filter = [[-1,0,1],[-2,0,2],[-1,0,1]]


print(img_arr)
width,height,d=img_arr.shape



for row in range (3,width-2):
    for col in range (3,height-2):
        local_pix=img_arr[row-1:row+2,col-1:col+2,0]
        transformed_pix=local_pix*vertical_filter
        vertiscore=transformed_pix.sum()/4
        
        transformed_pix_2=local_pix*hori_filter
        horiscore=transformed_pix_2.sum()/4
        edge_score=(vertiscore**2+horiscore**2)**.5
        vertical_edges[row,col]=[edge_score]*3
        
        
img2=Image.fromarray(np.uint8(vertical_edges))    
img2.show()    
        