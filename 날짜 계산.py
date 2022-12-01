e, s, m = map(int, input().split())

ed, sd, md = 0, 0, 0
answer = 0

while True:
    if ed == e and sd == s and md == m:
        print(answer)
        break

    ed += 1
    sd += 1
    md += 1
    answer += 1

    if ed > 15:
        ed = 1

    if sd > 28:
        sd = 1

    if md > 19:
        md = 1
