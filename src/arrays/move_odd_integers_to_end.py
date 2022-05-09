"""
Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.

Return any array that satisfies this condition.



Example 1:

Input: nums = [3,1,2,4]
Output: [2,4,3,1]
Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
Example 2:

Input: nums = [0]
Output: [0]


Constraints:

1 <= nums.length <= 5000
0 <= nums[i] <= 5000
"""


def sort_array_by_parity(nums: list):
	result = []
	if nums:
		if len(nums) == 1:
			result = nums
		else:
			odd_pivot = len(nums) - 1
			while odd_pivot >= 0 and nums[odd_pivot] % 2 != 0:
				odd_pivot -= 1

			if odd_pivot == -1:
				result = nums
			else:
				i = 0
				while i <= odd_pivot:
					while nums[i] % 2 != 0 and i <= odd_pivot:
						temp = nums[i]
						for k in range(i, odd_pivot):
							nums[k] = nums[k+1]
						nums[odd_pivot] = temp
						odd_pivot -= 1
					i += 1
				result.clear()
				result.extend(nums)
	return result


if __name__ == '__main__':
	a = [3,1,2,4]
	a = [3,1,1,4]
	a = [1,3]
	print(sort_array_by_parity(a))
