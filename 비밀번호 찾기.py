n, m = map(int, input().split())
site = {}
for _ in range(n):
    a, b = input().split()
    site[a] = b

for _ in range(m):
    print(site.get(input()))
