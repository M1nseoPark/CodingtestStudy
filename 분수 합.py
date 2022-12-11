a, b = map(int, input().split())
c, d = map(int, input().split())


ar = a * d + b * c
br = b * d

ta, tb = ar, br
while tb != 0:
    temp = ta
    ta = tb
    tb = temp % ta

print(ar // ta, br // ta)
