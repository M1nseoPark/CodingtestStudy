self = [True for _ in range(100000)]

for i in range(1, 10001):
    temp = i
    
    if i >= 10000:
        temp += i // 10000
        i %= 10000
    if i >= 1000:
        temp += i // 1000
        i %= 1000
    if i >= 100:
        temp += i // 100
        i %= 100
    if i >= 10:
        temp += i // 10
        i %= 10
    if i >= 1:
        temp += i // 1

    self[temp] = False

for i in range(1, 10001):
    if self[i]:
        print(i)

