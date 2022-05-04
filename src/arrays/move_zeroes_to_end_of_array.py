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
	if nums:
		num_zeroes = 0
		length_ = len(nums)
		if length_ > 1:
			set1 = list(set(nums))
			if len(set1) == 1:
				if set1[0] == 0:
					return
			for i in range(0, length_-1):
				while nums[i] == 0:
					if i >= length_ - num_zeroes:
						break
					for j in range(i, length_-1):
						nums[j] = nums[j+1]
					nums[length_-1] = 0
					num_zeroes += 1


if __name__ == '__main__':
	arr = [0,1,0,3,12]
	arr = [0,0,1]
	arr = [0,0,0]
	move_zeroes(arr)
	print(arr)





