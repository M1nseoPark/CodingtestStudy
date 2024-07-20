def solution(routes):
    answer = 0
    camera = -30001
    routes.sort(key=lambda x: x[1])
    
    for s, f in routes:
        if s > camera:
            answer += 1
            camera = f
    
    return answer


# [1, 10] [2, 10] [2, 3] [4, 5]
# 한 경로가 다른 경로를 포함하는 경우에는 틀림

# def solution(routes):
#     answer = 0
#     camera = 0
#     routes.sort()
    
#     for s, f in routes:
#         if s > camera or camera > f:
#             answer += 1
#             camera = f
    
#     return answer
