# i-1번 스티커를 뗐을 경우 = i번째 스티커는 뗄 수 없음 => table[i-1]값 그대로
# i-1번 스티커를 떼지 않았을 경우 = i-2번까지의 최댓값 + i번째 스티커의 값 
def solution(sticker):
    # 스티커가 1개일 경우
    if len(sticker) == 1:
        return sticker[0]

    # 1. 맨 앞 스티커를 떼는 경우
    table = [0 for _ in range(len(sticker))]
    table[0] = sticker[0]
    table[1] = table[0]

    for i in range(2, len(sticker)-1):
        table[i] = max(table[i-1], table[i-2] + sticker[i])

    value = max(table)

    # 2. 맨 앞 스티커를 떼지 않는 경우
    table = [0 for _ in range(len(sticker))]
    table[0] = 0
    table[1] = sticker[1]
    for i in range(2, len(sticker)):
        table[i] = max(table[i-1], table[i-2] + sticker[i])

    return max(value, max(table))

print(solution([5, 1, 16, 17, 16]))
