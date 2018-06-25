class Node:
	def __init__(self, x):
		self.value = x
		self.next = None

def get_kth_last_element(self, k):
	if k<0:
		return None
	curr1 = self
	curr2 = self
	for i in range (k+1):
		if not curr1:
			return None
		curr1 = curr1.next
	while curr1:
		curr1 = curr1.next
		curr2 = curr2.next
	return curr2.value

def main():
	n0 = Node(0)
	n1 = Node(1)
	n2 = Node(2)

	n0.next = n1
	n1.next = n2
	assert(get_kth_last_element(n0, 1) == 1) 
	assert(get_kth_last_element(n0, 2) == 0) 
	assert(not get_kth_last_element(n0, 3)) 

main()

main()
