class Node:
	def __init__(self, x):
		self.value = x
		self.next = None

def get_kth_last_element(k):
	if k<0:
		return None
	curr1 = self.head
	curr2 = self.head
	for i in range (k+1):
		if not curr1:
			return None
		curr1 = curr1.next
	while curr1:
		curr1 = curr1.next
		curr2 = curr2.next
	return curr2.value
