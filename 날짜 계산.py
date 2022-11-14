import sys

e, s, m = map(int, sys.stdin.readline().split())
ed, sd, md = 1, 1, 1

answer = 1
while True:
    if ed == e and sd == s and md == m:
        break

    ed += 1
    sd += 1
    md += 1
    answer += 1

    if ed >= 16:
        ed -= 15
    if sd >= 29:
        sd -= 28
    if md >= 20:
        md -= 19

print(answer)
