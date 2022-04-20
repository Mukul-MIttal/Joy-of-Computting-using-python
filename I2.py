import numpy as np
from PIL import Image
im=Image.open("b.jpg")
pixelmap=im.load()
I=np.asanyarray(Image.open("b.jpg"))
s=list(im.size)
s=[s[0]*2,s[1]*2]
s=tuple(s)
img=Image.new(im.mode,s)
pixelnew=img.load()


for i in range(im.size[0]):
    for j in range(im.size[1]):
        x=i*2
        y=j*2
        pixelnew[x-1,y-1]=pixelmap[i,j]
        pixelnew[x-1,y-2]=pixelmap[i,j]
        pixelnew[x-2,y-1]=pixelmap[i,j]
        pixelnew[x-2,y-2]=pixelmap[i,j]
img.save("b.jpg")
