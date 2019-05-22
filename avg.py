import os, numpy, PIL
from PIL import Image


path = 'Letters\\'
imlist = []
for r, d, f in os.walk(path):
    for file in f:
        imlist.append(os.path.join(r, file))


w,h=Image.open(imlist[0]).size
N=len(imlist)

arr=numpy.zeros((h,w,3),numpy.float)

for fil in imlist:
    im = Image.open(fil)
    im.load()
    background = Image.new("RGB", im.size, (255, 255, 255))

    background.paste(im, mask=im.split()[3])
    imarr = numpy.array(background,dtype=numpy.float)
    arr=arr+imarr/N


arr[arr !=[255, 255, 255]]-= 80
arr=numpy.array(numpy.round(arr),dtype=numpy.uint8)


out=Image.fromarray(arr,mode="RGB")
out.save("Average.png")
out.show()