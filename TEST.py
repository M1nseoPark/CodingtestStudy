temp = {1:2, 3:4}
arr = list(zip(temp.keys(), temp.values()))
arr.sort(key=lambda x:(x[1], x[0]))
print(list(sum(arr, ())))
