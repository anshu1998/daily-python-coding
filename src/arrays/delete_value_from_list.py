def delete_val(nums: list, val):
	if nums and val:
		for num in list(nums):
			if num == val:
				nums.remove(num)
		return len(nums)


def remove_duplicates(nums: list):
	if nums:
		r = {}
		for n in nums:
			if n in r:
				r[n] += 1
			else:
				r[n] = 1
		nums.clear()
		nums.extend(r.keys())
		return len(nums)


def is_duplicate_present(arr: list):
	if arr:
		for i, num in enumerate(arr):
			for j, double in enumerate(arr):
				if i == j:
					continue
				if double == 2*num:
					return True
		return False


def is_mountain_array(arr: list):
	result = False
	if arr and len(arr) >= 3:
		first_down = None
		first_up = None
		i = 0
		while i < len(arr) - 1:
			if arr[i+1] > arr[i]:
				if not first_up:
					first_up = True
				if first_down:
					return result
			elif arr[i+1] == arr[i]:
				return result
			else:
				if not first_up:
					return result
				if not first_down:
					first_down = True
			i += 1
		if first_up and first_down:
			result = True
	return result


if __name__ == '__main__':
	a = [0, 1, 2, 2, 3, 0, 4, 2]
	a = [0, 0]
	a = [2,1]
	a = [3,5,5]
	a = [0,3,2,1]
	a = [2,0,2]
	a = [0,3,2,1]
	a = [0,1,2,3,4,5,6,7,8,9]
	# a = [0,2,3,3,5,2,1,0]
	# a = [10,2,5,3]
	val = 2
	# k = delete_val(a, val)
	# k = remove_duplicates(a)
	# k = is_duplicate_present(a)
	k = is_mountain_array(a)
	print(a, k)
