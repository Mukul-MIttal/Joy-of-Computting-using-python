from PIL import Image 
'''
#flipping the image
img=Image.open("temp.jpg")
transposed_img=img.transpose(Image.FLIP_LEFT_RIGHT)
transposed_img.save("out.png")
'''
import cv2

img=cv2.imread("temp.png")

clahe=cv2.createCLAHE()

gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

enh_img=clahe.apply(gray_image)

cv2.imwrite("e.png",enh_img)