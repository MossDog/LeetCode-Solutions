from typing import List


class Solution:
	def two_sum(self, nums: List[int], target: int) -> List[int]:
		# Brute-force: check all pairs for the target sum
		for x in range(len(nums)):
			for y in range(x + 1, len(nums)):
				if nums[x] + nums[y] == target:
					return [x, y]