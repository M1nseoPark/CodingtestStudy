s = int(input())

answer = 0
result = 0
while True:
    if result == s:
        break

    if result > s and answer > (result - s):
        answer -= 1
        break
    else:
        answer += 1
        result += answer

print(answer)
