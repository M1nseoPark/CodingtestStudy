def merge_sort(arr):
	if len(arr) < 2:
		return arr
	
	# 리스트의 길이가 1이 될 때까지 리스트를 둘로 나누기
	mid = len(arr) // 2
	low_arr = merge_sort(arr[:mid])   # 재귀
	high_arr = merge_sort(arr[mid:])   # 재귀
	
	# 두 리스트를 합쳐서 정렬된 리스트 만들기
	merged_arr = []
	l = h = 0
	while l < len(low_arr) and h < len(high_arr):
		if low_arr[l] < high_arr[h]:
			merged_arr.append(low_arr[l])
			l += 1
		else:
			merged_arr.append(high_arr[h])
			h += 1

	merged_arr += low_arr[l:]
	merged_arr += high_arr[h:]

	return merged_arr

print(merge_sort([6, -8, 1, 12, 8, 15, 7, -7]))



    
    
