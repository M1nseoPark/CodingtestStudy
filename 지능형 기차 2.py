people = []
for _ in range(10):
    people.append(list(map(int, input().split())))

train = [people[0][1]]
for i in range(1, 10):
    train.append(train[-1] - people[i][0] + people[i][1])

print(max(train))
