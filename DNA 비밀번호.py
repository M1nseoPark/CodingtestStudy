s, p = map(int, input().split())
dna = input()
a, c, g, t = map(int, input().split())

kind = {}
kind['A'] = 0
kind['C'] = 0
kind['G'] = 0
kind['T'] = 0

left, right = 0, 0
kind[dna[0]] += 1
answer = 0

while left < s and right < s:
    if p == (right - left + 1):
        if kind['A'] >= a and kind['C'] >= c and kind['G'] >= g and kind['T'] >= t:
            answer += 1

        kind[dna[left]] -= 1
        left += 1
    else:
        right += 1
        if right < s:
            kind[dna[right]] += 1

print(answer)
