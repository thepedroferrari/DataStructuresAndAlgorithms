class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def to_list(self):
        out = []
        node = self.head
        while node:
            out.append(node.value)
            node = node.next
        return out


# Define a function outside of the class
def prepend(self, value):
    """ Prepend a value to the beginning of the list. """
    # TODO: Write function to prepend here

    if self.head is None:
        self.head = Node(value)

    else:
        current = self.head
        self.head = Node(value)
        self.head.next = current

    pass


def append(self, value):
    """ Append a value to the end of the list. """
    # TODO: Write function to append here
    if self.head is None:
        self.head = Node(value)

    else:
        current = self.head
        while current.next:
            current = current.next

        current.next = Node(value)
    pass


def search(self, value):
    """ Search the linked list for a node with the requested value and return the node. """
    # TODO: Write function to search here
    if self.head is None:
        return None

    current = self.head
    if current.value == value:
        return current

    while current.next:
        if current.value == value:
            return current
        else:
            current = current.next
    pass


def remove(self, value):
    print('removing')
    """ Remove first occurrence of value. """
    # TODO: Write function to remove here
    current = self.head

    if current is None:
        print('current is none')
        return

    if current.value == value:
        if current.next.next:
            current.value = current.next.value
            current.next = current.next.next
        else:
            current.value = None
            current.next = None
        return

    while current.next:
        if current.value == value:

            if current.next:
                current.value = current.next.value
                current.next = current.next.next
            else:
                current.next = None
            return

    pass


LinkedList.remove = remove
LinkedList.search = search
LinkedList.append = append
LinkedList.prepend = prepend

linked_list = LinkedList()

linked_list.append(2)
linked_list.append(1)
linked_list.append(1)
linked_list.append(3)
linked_list.append(4)
linked_list.append(3)

linked_list.remove(1)
assert linked_list.to_list() == [2, 1, 3, 4, 3], f"list contents: {linked_list.to_list()}"
linked_list.remove(3)
assert linked_list.to_list() == [2, 1, 4, 3], f"list contents: {linked_list.to_list()}"
linked_list.remove(3)
assert linked_list.to_list() == [2, 1, 4], f"list contents: {linked_list.to_list()}"