from typing import Optional


# Definition for singly-linked list.
class ListNode:
	def __init__(self, val = 0, next = None):
		self.val = val
		self.next = next


class Solution:
	def add_two_numbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
		# Initialize a dummy node to retain access to the head of the result list
		dummy = ListNode()
		current = dummy
		carry = 0

		# Traverse both linked lists until both are exhausted
		while l1 or l2 or carry:
			# Get the values of the current nodes, or 0 if the node is None
			val1 = l1.val if l1 else 0
			val2 = l2.val if l2 else 0

			# Calculate the sum and the carry
			total = val1 + val2 + carry
			carry = total // 10
			current.next = ListNode(total % 10)

			# Move to the next nodes
			current = current.next
			
			if l1:
				l1 = l1.next
				
			if l2:
				l2 = l2.next

		return dummy.next