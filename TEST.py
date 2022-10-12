for i in range(0, 4, 4):
    for j in range(0, 4, 4):
        for y in range(4):
            for x in range(4):
                print(y+j, x+4-i-1, i+y, j+x)
            print('-----')
        
