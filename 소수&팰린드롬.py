n = int(input())

arr = [True for _ in range(10000000)]
arr[1] = False

for i in range(2, int(10000000**0.5)+1):
    if arr[i]:
        for j in range(i+i, 10000000, i):
            arr[j] = False

k = n
while True:
    temp = str(k)
    
    if arr[k] and temp == temp[::-1]:
        print(k)
        break

    k += 1
