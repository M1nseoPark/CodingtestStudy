n = int(input())
number = list(map(int, input().split()))

number.sort()
print(number[0], number[-1])
