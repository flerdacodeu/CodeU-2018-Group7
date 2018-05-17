class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, value):
        """
        Push value to the head of the list
        """

        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def find_kth_last_element(self, k):
        """
        Return the kth to last element of the list
        k = 0 - the last element, e.t.c.

        :return None if list is empty or k+1 > len(list) else the kth to last element
        """

        first_ptr = self.head
        i = 0
        if self.head is None:
            print("Input list is empty")
            return
        else:
            while i < k + 1:
                if first_ptr is None:
                    print("Length of list is shorter than {k}".format(k=k+1))
                    return
                first_ptr = first_ptr.next
                i += 1

            second_ptr = self.head
            while first_ptr is not None:
                first_ptr = first_ptr.next
                second_ptr = second_ptr.next
            return second_ptr
