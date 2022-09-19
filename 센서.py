n = int(input())
k = int(input())
sensor = list(map(int, input().split()))

sensor.sort()
receive = []
for i in range(n-1):
    receive.append(sensor[i+1] - sensor[i])

receive.sort()

if k >= n:   # 집중국이 센서보다 많을 수도 있음 -> 조건 잘 확인하기
    print(0)
else:
    for i in range(k-1):
        receive.pop()

    print(sum(receive))
