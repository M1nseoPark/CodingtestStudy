a = int(input())
b = int(input())
c = int(input())

rst = str(a * b * c)
ans = [0] * 10

for i in range(len(rst)):
    ans[int(rst[i])] += 1

for i in range(10):
    print(ans[i])
