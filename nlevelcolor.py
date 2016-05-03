from PIL import Image
from PIL import ImageDraw

PixScale=512

im = Image.new("RGB",(PixScale,PixScale),"black")
d = ImageDraw.Draw(im)

N = 3
NColors = pow(N,3)
NColumns = int(pow(NColors,0.5))+1
NRows = NColumns
w=PixScale/NColumns
h=PixScale/NRows


for i in range(0,NColors):
	x=(i%NColumns)*w
	y=((i/NColumns))*h
	r=(i%N)*(255/(N-1))
	g=((i/N)%N)*(255/(N-1))
	b=((i/(N*N))%N)*(255/(N-1))
	d.rectangle([x,y,x+w,y+h],fill=(r,g,b))
	#print("R: " + str(r) + " G: " + str(g) + " B: " +str(b))
	#print("X: " + str(x) + " Y: " + str(y))

im.save("test.png","PNG")