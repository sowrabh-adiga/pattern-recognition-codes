from PIL import Image, ImageFilter
 
if __name__=="__main__":
	im = Image.open("/home/sowrabh/Desktop/8th sem/pattern-20191103T061324Z-001/pattern/Kat.png")
 
	kernelValues = [0,-1,0,
					-1,7,-1,
					0,-1,0] #emboss
	kernel = ImageFilter.Kernel((3,3), kernelValues)
 
	im2 = im.filter(kernel)
 
	im2.show()
	im.show()