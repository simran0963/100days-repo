import math
def paint_calc(height,width,cover): 
	no_of_can=(height*width)/coverage 
	can=math.ceil(no_of_can) 
	print(f"no. of can required are :{can}")

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
