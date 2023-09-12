# n번째 유사 칸토어 비트열 
# 1 ≤ l, r ≤ 5^n
def solution(n, l, r):
    # end까지의 1의 개수를 구하는 함수 
    def count(n, end):
        if n == 1:
            return "11011"[:end].count("1")
        
        a, b = divmod(end, 5**(n-1))
        if a <= 1:
            return 4**(n-1) * a + count(n-1, b)
        elif a == 2:
            return 2 * 4**(n-1)
        else:
            return 4**(n-1) * (a-1) + count(n-1, b)
        
    return count(n, r) - count(n, l-1)