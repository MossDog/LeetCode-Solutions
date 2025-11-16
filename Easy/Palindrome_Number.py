class Solution:
	def is_palindrome(self, x: int) -> bool:
		
		# Negative numbers are not palindromes
		if x < 0:		
			return False

		str_x = str(x)
		
		# Check if the string is the same forwards and backwards
		if str_x == str_x[::-1]:
			return True
		
		return False