for row in range (0,10):
	for space in range(0,9-row):
		print(" ",end=" ")
	for col in range (0,row+1):
	    print("*",end=" ")
	print()  
for row in range (0,10):
	for space in range (0,row+1):
		print(" ",end=" ")
	for col in range(0,9-row):
	    print("*",end=" ")
	print() 	