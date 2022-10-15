# 97 a, 122 z
s = input()
ans = [0] * 26

for i in range(len(s)):
    ans[ord(s[i])-97] += 1

print(' '.join(map(str, ans)))
