from itertools import combinations

def count(line1, line2):
    a1, b1, c1 = line1
    a2, b2, c2 = line2

    if a1 * b2 == b1 * a2:
        return None

    x = (b1*c2-c1*b2) / (a1*b2-b1*a2)
    y = (c1*a2-a1*c2) / (a1*b2-b1*a2)

    if x == int(x) and y == int(y):
        return [int(x), int(y)]


def solution(line):
    points = set()
    for c in combinations(line, 2):
        point = count(c[0], c[1])
        if point:
            points.add(point)

    # 교점의 x좌표들 
    xs = [p[0] for p in points]
    x_min = min(xs)
    x_max = max(xs)

    # 교점의 y좌표들 
    ys = [p[1] for p in points]
    y_min = min(ys)
    y_max = max(ys)

    answer = ['.' * (x_max-x_min+1)] * (y_max-y_min+1)
    for point in points:
        x, y = point
        answer[y_max-y] = answer[y_max-y][:x-x_min] + '*' + answer[y_max-y][x-x_min+1:]

    return [''.join(ans) for ans in answer]


    
        
    
