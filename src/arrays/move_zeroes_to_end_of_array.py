"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.



Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]


Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1
"""


def move_zeroes(nums: list):
	pivot = len(nums) - 1
	while pivot >= 0 and nums[pivot] == 0:
		pivot -= 1

	if pivot == -1:
		return

	i = 0
	while i <= pivot:
		while nums[i] == 0 and i <= pivot:
			for k in range(i, pivot):
				nums[k] = nums[k+1]
			nums[pivot] = 0
			pivot -= 1
		i += 1


if __name__ == '__main__':
	arr = [0,1,0,3,12]
	# arr = [0,0,1]
	# arr = [0,0,0]
	move_zeroes(arr)
	print(arr)





