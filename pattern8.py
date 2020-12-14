for row in range(0,5):
    for space in range(0,4-row):
        print(" ",end=" ")
    for col in range (0,2*row+1):
        print("*",end=" ")
    print() 
for row in range (0,5):
    for space in range(0,row+1):
        print(" ",end=" ")
    for col in range(0,7-2*row):
        print("*",end=" ")
    print()     
    