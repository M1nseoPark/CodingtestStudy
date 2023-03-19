import sys
sys.setrecursionlimit(1000000)


def preorder(arrY, answer):  # 루트->왼->오 
    root = arrY[0]
    left = []
    right = []

    for i in range(1, len(arrY)):
        if root[0] > arrY[i][0]:   # 루트의 x좌표 > x좌표 -> 루트 기준 왼쪽 
            left.append(arrY[i])
        else:
            right.append(arrY[i])

    answer.append(root[2])
    if len(left) > 0:
        preorder(left, answer)
    if len(right) > 0:
        preorder(right, answer)

    return


def postorder(arrY, answer):   # 왼->오->루트 
    root = arrY[0]
    left = []
    right = []

    for i in range(1, len(arrY)):
        if root[0] > arrY[i][0]:
            left.append(arrY[i])
        else:
            right.append(arrY[i])

    if len(left) > 0:
        postorder(left, answer)
    if len(right) > 0:
        postorder(right, answer)
    answer.append(root[2])

    return

    
def solution(nodeinfo):
    answer1 = []   # preorder
    answer2 = []   # postorder

    # nodeinfo는 1번 노드부터 노드 좌표(x,y)가 들어있는 배열 -> 노드 번호를 추가해줌([5, 3, 1])
    for i in range(len(nodeinfo)):
        nodeinfo[i].append(i+1)

    arrY = sorted(nodeinfo, key=lambda x:(-x[1], x[0]))  # y 기준 내림차순

    preorder(arrY, answer1)
    postorder(arrY, answer2)

    return [answer1, answer2]

    
        
