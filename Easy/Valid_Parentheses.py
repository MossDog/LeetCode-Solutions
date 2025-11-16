class Solution:
	def is_valid(self, s: str) -> bool:
		# Stack to keep track of opening brackets
		stack = []
		# Mapping of closing to opening brackets
		mapping = {')': '(', '}': '{', ']': '['}
		
		for char in s:
			
			if char in mapping.values():
				# Push opening brackets onto the stack
				stack.append(char)
				
			elif char in mapping:
				# If stack is empty or top doesn't match, it's invalid
				if not stack or stack[-1] != mapping[char]:
					return False
				
				# Pop the matched opening bracket
				stack.pop()
				
		# If stack is empty, all brackets matched
		return not stack
