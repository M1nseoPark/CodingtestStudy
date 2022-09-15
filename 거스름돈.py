money = int(input())
change = 1000 - money

answer = 0
if change >= 500:
    answer += (change // 500)
    change = change % 500
if change >= 100:
    answer += (change // 100)
    change = change % 100
if change >= 50:
    answer += (change // 50)
    change = change % 50
if change >= 10:
    answer += (change // 10)
    change = change % 10
if change >= 5:
    answer += (change // 5)
    change = change % 5
if change >= 1:
    answer += change

print(answer)
