n, m = map(int, input().split())
brand = []
for _ in range(m):
    brand.append(list(map(int, input().split())))

answer = []
answer.append((n // 6 + 1) * min(r[0] for r in brand))   # 세트만 사는 경우
answer.append(((n // 6) * min(r[0] for r in brand)) +
              ((n % 6) * min(r[1] for r in brand)))   # 딱 맞춰서 사는 경우

answer.append(n * min(r[1] for r in brand))   # 낱개로만 사는 경우

print(min(answer))
