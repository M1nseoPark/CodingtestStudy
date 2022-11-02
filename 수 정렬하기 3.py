# for문 속에서 append를 사용하게 되면 재할당이 이루어져서
# 메모리를 효율적으로 사용 못함!
import sys

n = int(sys.stdin.readline())
arr = [0 for _ in range(10001)]

for _ in range(n):
    arr[int(sys.stdin.readline())] += 1

for i in range(10001):
    if arr[i] != 0:
        for j in range(arr[i]):
            print(i)
