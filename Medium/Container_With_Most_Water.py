
from typing import List


class Solution:
	def max_area(self, height: List[int]) -> int:
		# max_vol stores the maximum area found
		max_vol = 0
		# Two pointers at the start and end of the array
		left = 0
		right = len(height) - 1

		while left < right:
			# Calculate area between the two lines
			max_vol = max(max_vol, (right - left) * min(height[left], height[right]))

			# Move the pointer at the shorter line inward
			if height[left] < height[right]:
				left += 1
			else:
				right -= 1

		return max_vol