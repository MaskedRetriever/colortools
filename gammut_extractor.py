#!/usr/bin/python
#Gammut Extractor
#Splat down duplicates of N pixels
#rearranged onto the gammut circle

try:
    import Image
    import ImageDraw
except ImportError:
    from PIL import Image
    from PIL import ImageDraw
import math, random, colorsys, sys
    
N=10000
ImageFile=sys.argv[1]
r=1
size=400
    
img = Image.open(ImageFile)
outimg = Image.new("RGB",(size,size),"black")
d=ImageDraw.Draw(outimg)
hsv_pix=[]
for pixel in random.sample(img.getdata(),N):
    hsv_pix.append(colorsys.rgb_to_hsv(pixel[0]/255.0,
                            pixel[1]/255.0,
                            pixel[2]/255.0))
for hsv in sorted(hsv_pix,key=lambda b:b[2]):
#for hsv in hsv_pix:
    pixel=colorsys.hsv_to_rgb(hsv[0],hsv[1],hsv[2])
    pixel=(int(pixel[0]*255),int(pixel[1]*255),int(pixel[2]*255))
    
    XPos = (size*.5)+size*.5*hsv[1]*math.cos(hsv[0]*2*math.pi)
    YPos = (size*.5)+size*.5*hsv[1]*math.sin(hsv[0]*2*math.pi)

    r=int((1.2-hsv[2])*10)
    d.ellipse((XPos-r,YPos-r,XPos+r,YPos+r),fill=pixel)

OutFile="/tmp/out"+str(int(random.random()*1000000))+".png"
outimg.save(OutFile)

    