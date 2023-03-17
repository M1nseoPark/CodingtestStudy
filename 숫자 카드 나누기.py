import math

def solution(arrayA, arrayB):
    arrayA = list(set(arrayA))
    gcdA = arrayA[0]
    for i in range(1, len(arrayA)):
        gcdA = math.gcd(gcdA, arrayA[i])

    arrayB = list(set(arrayB))
    gcdB = arrayB[0]
    for i in range(1, len(arrayB)):
        gcdB = math.gcd(gcdB, arrayB[i])

    for i in arrayA:
        if i % gcdB == 0:
            gcdB = 1
            break

    for i in arrayB:
        if i % gcdA == 0:
            gcdA = 1
            break

    if gcdA == 1:
        if gcdB == 1:
            return 0
        else:
            return gcdB
    else:
        if gcdB == 1:
            return gcdA
        else:
            return max(gcdA, gcdB)
