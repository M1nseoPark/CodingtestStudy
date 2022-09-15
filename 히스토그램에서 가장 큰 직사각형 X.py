def histogram(fence, left, right):
    if left == right:
        return fence[left]

    mid = (left + right) // 2
    lo = mid
    hi = mid + 1

    ret = max(histogram(fence, left, lo), histogram(fence, hi, right))

    height = min(fence[lo], fence[hi])   
    ret = max(ret, 2 * height)   
    while left <= lo and hi <= right:
        if hi < right and (left == lo or fence[lo - 1] <= fence[hi + 1]):
            hi += 1
            height = min(height, fence[hi])
        else:
            lo -= 1
            height = min(height, fence[lo])

        ret = max(ret, height * (hi - lo + 1))

    return ret


while True:
    fence = list(map(int, input().split()))

    if fence[0] == 0:
        break

    print(histogram(fence, 1, fence[0]))
