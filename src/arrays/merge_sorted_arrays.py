"""
Merge two almost sorted arrays

a = [3, 4, 10, 0, 0, 0], m = 3
b = [1, 3, 5], n = 3
result, a = [1, 3, 3, 4, 5, 10]

a = [], m = 0
b = [1, 4], n = 2
result, a = [1, 4]

a = [1], m = 1
n = [], n = 0
result, a = [1]

a is array of length m+n
b is array of length n
m = number of nonzero elements in the array 'a'
"""


def merge_arrays(nums1, nums2, m, n):
	result = []
	i = j = 0
	while i < m and j < n:
		if nums1[i] <= nums2[j]:
			result.append(nums1[i])
			i += 1
		else:
			result.append(nums2[j])
			j += 1
	while i < m:
		result.append(nums1[i])
		i += 1
	while j < n:
		result.append(nums2[j])
		j += 1
	nums1.clear()
	nums1.extend(result)


def merge_arrays2(nums1, nums2, m, n):
	j = k = 0
	l = m + n
	if m == 0:
		nums1.clear()
		nums1.extend(nums2)
	elif n == 0:
		pass
	else:
		for i in range(0, l-1):
			if nums2[j] <= nums1[i]:
				for k in range(l-1, i, -1):
					nums1[k] = nums1[k-1]
				nums1[k-1] = nums2[j]
				j += 1


if __name__ == '__main__':
	a = [3, 4, 10, 0, 0, 0]
	# a = [3]
	# a = [0]
	b = [1, 3, 5]
	# b = []
	# b = [1]
	m = 3
	# m = 1
	# m = 0
	n = 3
	# n = 0
	# n = 1
	# merge_arrays(a, b, m, n)
	merge_arrays2(a, b, m, n)
	print(a)
