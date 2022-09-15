n = int(input())
meeting = []
answer = []

for _ in range(n):
    s, f = map(int, input().split())
    meeting.append([s, f])

meeting.sort(key=lambda x:(x[1], x[0]))
answer.append(meeting[0])

for i in range(1, n):
    if answer[-1][1] <= meeting[i][0]:
        answer.append(meeting[i])

print(len(answer))

