n = int(input())

def draw(n):
    if n == 3:
        return ['  *  ', ' * * ', '*****']

    star = draw(n//2)
    l = []
    
    for s in star:
        l.append(' '*(n//2) + s + ' '*(n//2))

    for s in star:
        l.append(s + ' ' + s)

    return l

print('\n'.join(draw(n)))
