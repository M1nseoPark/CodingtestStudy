n = int(input())

def draw(n):
    if n == 1:
        return ['*']

    star = draw(n//3)   # n=3일 때 draw(1) -> star=['*']
    l = []

    for s in star:
        l.append(s * 3)
    for s in star:
        l.append(s + ' ' * (n//3) + s)
    for s in star:
        l.append(s * 3)

    return l
    

print('\n'.join(draw(n)))
