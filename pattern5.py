for row in range(0,19):
    if row < 10 :
        for space in range(0,9-row):
         print(" ",end=" ")
        for col in range (0,row+1):
         print("*",end=" ")
    else:
        for space in range (0,row-9):
           print(" ",end=" ")
        for col in range(0,19-row):
           print("*",end=" ")
    print()               