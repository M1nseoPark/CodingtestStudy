n, r, c = map(int, input().split())  # r행 c열

# 2^n x 2^n 배열에서 (r, c)를 방문하는 순서를 반환하는 함수
def func(n, r, c):
    if n == 0:
        return 0

    half = (2 ** n) // 2

    if r < half and c < half:
        return func(n-1, r, c)

    elif r < half and c >= half:
        return half * half + func(n-1, r, c-half)

    elif r >= half and c < half:
        return 2 * half * half + func(n-1, r-half, c)

    else:
        return 3 * half * half + func(n-1, r-half, c-half)

print(func(n, r, c))

    
    
