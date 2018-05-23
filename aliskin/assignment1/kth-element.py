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

def construct_linked_list(elements):
    """
    Input should be a list or a string
    """
    head = ListNode(elements[0])
    prev = head
    for elem in elements[1:]:
        new_node = ListNode(elem)
        prev.next = new_node
        prev = prev.next
    return head

def main():
    elements = range(10)
    linked_list = construct_linked_list(elements)
    for k in range(len(elements)):
        value = kth_last_element(linked_list, k).value
        assert (value == elements[-1 - k]), '{} is not equal to {}'.format(value, elements[-1 -k])

    letters = "abcdefghijklmnopqrstuwxyz"
    linked_list = construct_linked_list(letters)
    for k in range(len(letters)):
        value = kth_last_element(linked_list, k).value
        assert (value == letters[-1 - k]), '{} is not equal to {}'.format(value, letters[-1 -k])

if __name__ == "__main__":
    main()
