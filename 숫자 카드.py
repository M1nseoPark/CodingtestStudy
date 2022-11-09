n = int(input())
card = list(map(int, input().split()))
m = int(input())
arr = list(map(int, input().split()))

card.sort()

def find(k):
    left = 0
    right = n - 1

    while left <= right:
        mid = (left + right) // 2

        if card[mid] == k:
            return 1

        elif card[mid] > k:
            right = mid - 1

        else:
            left = mid + 1

    return 0

answer = []
for i in range(m):
    answer.append(find(arr[i]))

print(' '.join(map(str, answer)))
    
