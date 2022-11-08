n, k = map(int, input().split())

arr = [i for i in range(1, n+1)]
data = ''.join(map(str, arr))

if len(data) < k:
    print(-1)
else:
    print(data[k-1])
