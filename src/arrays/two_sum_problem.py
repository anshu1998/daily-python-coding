"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.



Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]


Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.

"""


def merge_sort(nums: list):
	if len(nums) > 1:
		mid = len(nums)//2
		left = nums[:mid]
		right = nums[mid:]
		merge_sort(left)
		merge_sort(right)
		ll = len(left)
		lr = len(right)
		i = j = k = 0

		while i < ll and j < lr:
			if left[i] <= right[j]:
				nums[k] = left[i]
				i += 1
			else:
				nums[k] = right[j]
				j += 1
			k += 1

		while i < ll:
			nums[k] = left[i]
			i += 1
			k += 1

		while j < lr:
			nums[k] = right[j]
			j += 1
			k += 1


def two_sum(nums: list, goal: int):
	if nums:
		nums2 = nums.copy()
		merge_sort(nums2)
		i = 0
		j = len(nums2) - 1
		while i != j:
			sum_ = nums2[i] + nums2[j]
			if sum_ == goal:
				return [nums[i], nums[j]]
			elif sum_ > goal:
				j -= 1
			else:
				i += 1


if __name__ == '__main__':
	# arr = [3, 2, 4]
	arr = [2,7,11,15]
	# arr = [3,3]
	# t = 6
	t = 9
	# t = 6
	print(two_sum(arr, t))
