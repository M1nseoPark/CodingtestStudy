costs = [[1, 7, 6, 7, 5, 4, 5, 3, 2, 3],
         [7, 1, 2, 4, 2, 3, 5, 4, 5, 6],
         [6, 2, 1, 2, 3, 2, 3, 5, 4, 5],
         [7, 4, 2, 1, 5, 3, 2, 6, 5, 4],
         [5, 2, 3, 5, 1, 2, 4, 2, 3, 5],
         [4, 3, 2, 3, 2, 1, 2, 3, 2, 3],
         [5, 5, 3, 2, 4, 2, 1, 5, 3, 2],
         [3, 4, 5, 6, 2, 3, 5, 1, 2, 4],
         [2, 5, 4, 5, 3, 2, 3, 2, 1, 2],
         [3, 6, 5, 4, 5, 3, 2, 4, 2, 1]]

def solution(numbers):
    dic = {}
    dic[(4, 6)] = 0   # 초기 상태에서 가중치는 0 
    
    for n in numbers:
        cur = {}
        for k, w in dic.items():
            left, right = k
            if right == int(n):   # 현재 오른쪽 손가락 위치 = 눌러야 할 숫자
                if (not (left, int(n)) in cur) or cur[(left, int(n))] > w + 1:
                    cur[(left, int(n))] = w + 1

            elif left == int(n):   # 현재 왼쪽 손가락 위치 = 눌러야 할 숫자
                if (not (int(n), right) in cur) or cur[(int(n), right)] > w + 1:
                    cur[(int(n), right)] = w + 1

            else:
                # 오른쪽으로 눌렀을 때 
                if (not (left, int(n)) in cur) or cur[(left, int(n))] > w + costs[right][int(n)]:
                    cur[(left, int(n))] = w + costs[right][int(n)]

                # 왼쪽으로 눌렀을 때 
                if (not (int(n), right) in cur) or cur[(int(n), right)] > w + costs[left][int(n)]:
                    cur[(int(n), right)] = w + costs[left][int(n)]

        dic = cur

    return min(list(dic.values()))

print(solution("1756"))
                
'''
dic 결과
{(4, 1): 5, (1, 6): 2}
{(4, 7): 9, (7, 1): 7, (1, 7): 7, (7, 6): 6}
{(4, 5): 12, (5, 7): 10, (7, 5): 8, (5, 1): 10, (1, 5): 10, (5, 6): 9}
{(4, 6): 14, (6, 5): 13, (5, 6): 10, (6, 7): 12, (7, 6): 10, (6, 1): 12, (1, 6): 12}
{(4, 6): 14, (6, 5): 13, (5, 6): 10, (6, 7): 12, (7, 6): 10, (6, 1): 12, (1, 6): 12}
'''
