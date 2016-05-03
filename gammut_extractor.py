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
    
N=3000
ImageFile=sys.argv[1]

    
img = Image.open(ImageFile)
outimg = Image.new("RGB",(200,200),"black")
d=ImageDraw.Draw(outimg)
for pixel in random.sample(img.getdata(),N):
    hsv=colorsys.rgb_to_hsv(pixel[0]/255.0,
                            pixel[1]/255.0,
                            pixel[2]/255.0)
    XPos = 100.0+100.0*hsv[1]*math.cos(hsv[0]*2*math.pi)
    YPos = 100.0+100.0*hsv[1]*math.sin(hsv[0]*2*math.pi)
    d.point((XPos,YPos),fill=pixel)
outimg.save("out.png","PNG")
    
    