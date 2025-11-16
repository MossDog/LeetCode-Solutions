class Solution:
	def length_of_longest_substring(self, s: str) -> int:
		# result stores the maximum length found
		result = 0
		# left is the start index of the current window
		left = 0
		# uniques is a set of unique characters in the current window
		uniques = set()
		
		for right in range(len(s)):
			# If s[right] is already in the set, shrink window from the left
			while s[right] in uniques:
				
				uniques.remove(s[left])
				left += 1
				
			# Add the current character to the set
			uniques.add(s[right])
			
			# Update the result if the current window is larger
			result = max(result, right - left + 1)
			
		return result