class ListNode:
    def __init__(self, x):
        self.value = x
        self.next = None

def kth_element(head, k):
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
