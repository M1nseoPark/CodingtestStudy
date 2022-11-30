n = int(input())

turn = (n // 3) + (n % 3)

if turn % 2 == 0:
    print('CY')
else:
    print('SK')
        
