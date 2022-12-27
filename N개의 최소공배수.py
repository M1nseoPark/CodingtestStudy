def solution(arr):
    a, b = max(arr[0], arr[1]), min(arr[0], arr[1])
    while b != 0:
	    temp = a
	    a = b
	    b = temp % a
        
    a = arr[0] * arr[1] // a
    print(a)
        
    if len(arr) > 2:
        for i in range(2, len(arr)):
            c, d = max(arr[i], a), min(arr[i], a)
            while d != 0:
                temp = c
                c = d
                d = temp % c
            a = arr[i] * a // c
            
    return a
