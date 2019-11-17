from PIL import Image, ImageFilter
 
if __name__=="__main__":
	im = Image.open("/home/Desktop/Kat.png")
 
	kernelValues = [0,-1,0,
					-1,7,-1,
					0,-1,0] #emboss
	kernel = ImageFilter.Kernel((3,3), kernelValues)
 
	im2 = im.filter(kernel)
 
	im2.show()
	im.show()
