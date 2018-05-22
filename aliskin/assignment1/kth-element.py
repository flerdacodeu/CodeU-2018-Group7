class ListNode:
    def __init__(self, x):
        self.value = x
        self.next = None

def kth_last_element(head, k):
    current = head
    length = 0
    while current is not None:
        length += 1
        current = current.next
    if (k >= length or k < 0):
        return None
    current = head
    i = 0
    while i < length - k - 1:
        current = current.next
        i += 1
    return current

head = ListNode(1)
prev = head
for i in range(2, 6):
    new_node = ListNode(i)
    prev.next = new_node
    prev = new_node

print(kth_last_element(head, 0).value)

letters = "abcdefghijklmnopqrstuwxyz"
head = ListNode('a')
prev = head
for symbol in letters[1:]:
    new_node = ListNode(symbol)
    prev.next = new_node
    prev = new_node

print(kth_last_element(head, 4).value)
