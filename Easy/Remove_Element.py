from typing import List


class Solution:
	def remove_element(self, nums: List[int], val: int) -> int:
		# Pointer for the next position to place a non-val element
		non_val_index = 0

		for i in range(len(nums)):
			if nums[i] != val:
				# Place non-val element at the next position
				nums[non_val_index] = nums[i]
				non_val_index += 1

		# Return the count of non-val elements
		return non_val_index
