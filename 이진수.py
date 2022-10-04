test = int(input())
for _ in range(test):
    n = int(input())

    binary = []
    while n != 1:
        binary.append(n % 2)
        n = n // 2

    binary.append(1)

    for i in range(len(binary)):
        if binary[i] == 1:
            print(i, end=' ')
'''
T = int(input())

for _ in range(T):
    n = bin(int(input()))[2:]
    print(type(n))
    for i in range(len(n)):
        if n[-i-1] == '1':
            print(i, end = " ")
'''

            
