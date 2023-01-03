m, n, k = map(int, input().split())
secret = list(map(int, input().split()))
user = list(map(int, input().split()))

answer = False
for i in range(n):
    if user[i:i+m] == secret:
        answer = True
        break

if answer:
    print('secret')
else:
    print('normal')
