import PIL
import numpy as np
from PIL import Image


#abhay mamgain 2021A4PS2188P , i just took pixels and their neighbouring pixels and averaged their r,g,b values 
# here i took a neighbourhood of 3 pixels but we can blur it more if we change it to 4 and i have to make a few changes then it will blur even more 
#pseudo code image input->def height width->def fn for averaging the rgb values -> write a for loop for selecting all the pixels leaving 3 pixel gap from 
#gap from extreame ends so that valid pixels are considered for averaging

# def blur_pixel(img,x,y):
#     r_tot=b_tot=g_tot=0
#     for x_new in range (x-3,x+3):
#         for y_new in range(y-3,y+3):
#             r,g,b = img.getpixel((x_new,y_new))
#             r_tot=r_tot+r
#             g_tot=g_tot+g
#             b_tot=b_tot+b
            
#     r_avg=r_tot//49 
#     g_avg=g_tot//49
#     b_avg=b_tot//49   
#     return(r_avg,g_avg,b_avg)    

# img = Image.open(r"C:\Users\Abhay\Desktop\robocon recruit\Recruitment-22\Image_Processing\Task_1\Blur\hills.jpg")
# print(img.getpixel((0,0)))

# height = img.size[1]
# width = img.size[0]
# img_blur=Image.new("RGB",(width,height),(0,0,0))




# for x in range (3,width-2):
#     for y in range (3,height-2):
#         r,g,b = img.getpixel((x,y))
#         r_new,g_new,b_new=blur_pixel(img,x,y)
#         img_blur.putpixel((x,y),(r_new,g_new,b_new))
        
# img_blur.show()



#------------------------------------------------just realised that we were supposed use arrays -----------------------------------
# def sum(i,j):
#     for k in range(-1,2):
#                 for m in range(-1,2):
#                     img[i,j]=img[i,j]+img[i+k,j+m]
#     nimg=img[i,j]//9
#     return nimg   

#i was wanting to take the average of pixels in neighbours like 8 ,but image was comming black i dont know why some kind of error in my understanding             
def blur(img):
    for i in range(2,img.shape[0]-2):
        for j in range(2,img.shape[1]-2):
            # img[i,j]=sum(i,j)
            #tried putting a loof some kind of error i think operation on arrays is not right on my part but this code blurs image-------------
                    
            img[i,j] = (img[i,j]*.111 + img[i-1,j]*.111 + img[i+1,j]*.111 + img[i,j-1]*.111 + img[i,j+1]*.111+ img[i-2,j]*.111+img[i+2,j]*.111+img[i,j+2]*.111+img[i,j-2]*.111)
    return img
# def blur(img):
#     for i in range (3,img.shape[0]-3):
#         for j in range (3,img.shape[1]-3):


            

img = np.array(Image.open(r'C:\Users\Abhay\Desktop\robocon recruit\Recruitment-22\Image_Processing\Task_1\Blur\hills.jpg'))

blur(img)

im = Image.fromarray(np.uint8(img))

im.show()

    
