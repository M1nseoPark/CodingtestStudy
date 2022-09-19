n = int(input())

result = n // 5
answer = False
while result != 0:
    if (n - (result * 5)) % 2 == 0:
        result += (n - (result * 5)) // 2
        answer = True
        break

    result -= 1

if not answer:
    if n % 2 == 0:
        print(n // 2)
    else:
        print(-1)
else:
    print(result)
