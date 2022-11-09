import bisect

n = int(input())
card = list(map(int, input().split()))
m = int(input())
arr = list(map(int, input().split()))

card.sort()

answer = []
for i in range(m):
    answer.append(bisect.bisect_right(card, arr[i]) - bisect.bisect_left(card, arr[i]))

print(' '.join(map(str, answer)))

