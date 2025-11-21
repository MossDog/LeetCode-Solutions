from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        write = 1  # index where the next unique number will be written

        for scan in range(1, len(nums)):
            if nums[scan] != nums[scan - 1]:
                nums[write] = nums[scan]
                write += 1

        return write