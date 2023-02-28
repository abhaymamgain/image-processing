import PIL.Image as Image
import numpy as np



#i tried a logic that i will take the horizontal projection aND vertical projection of the image and then by comparing the max value 
# in both arrays i will get either up down or left right then i just used width and height by 2 as reference for central index and if
# index of the max value was left then left and so on


# this only works on central arrow which looks normal .



img_arrow_1=np.array(Image.open(r"C:\Users\Abhay\Desktop\robocon recruit\Recruitment-22\Image_Processing\Task_2_Arrows\Arrow_1.jpg"))

width, height,d = img_arrow_1.shape
print(img_arrow_1.shape)

for row in range (0,width):
    for col in range (0,height):
       if img_arrow_1[row,col,0]>128 : img_arrow_1[row,col]=1 
       else :img_arrow_1[row,col]=0

v_projection = np.sum(img_arrow_1[:,:,0],axis=0)
h_projection = np.sum(img_arrow_1[:,:,0],axis=1)
print(np.where(v_projection==max(v_projection))[0][-1])





if max(h_projection) > max(v_projection):
    if np.where(h_projection==max(h_projection))[0][-1] < width / 2:
        print('Arrow is pointing left')
    else:
        print('Arrow is pointing right')
else:
    if np.where(v_projection==max(v_projection))[0][-1] < height / 2:
        print('Arrow is pointing up')
    else:
        print('Arrow is pointing down')


