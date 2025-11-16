from typing import List


class Solution:
	def longest_common_prefix(self, strs: List[str]) -> str:
		# Start with the first string as the prefix
		prefix = strs[0]
            
		for i in range(1, len(strs)):

			# Reduce the prefix until it matches the start of strs[i]
			while not strs[i].startswith(prefix):
				prefix = prefix[:-1]

				if len(prefix) == 0:
					return ""
                
		return prefix