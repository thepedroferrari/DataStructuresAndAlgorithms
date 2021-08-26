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
    # My solution requires two steps, Udacity does it all in one by checking Node instead of node.next
    # if current.value == value:
    #     return current
    #
    # while current.next:
    #     if current.value == value:
    #         return current
    #     else:
    #         current = current.next
    while current:
        if current.value == value:
            return current
        current = current.next

    # Udacity Code: Good to return error messages
    raise ValueError("Value not found in the list.")

    pass


def remove(self, value):
    print('removing')
    """ Remove first occurrence of value. """
    # TODO: Write function to remove here
    current = self.head

    if current is None:
        return

    if current.value == value:
        if current.next.next:
            current.value = current.next.value
            current.next = current.next.next
        else:
            current.value = None
            current.next = None
        return

    # For the above IF statement, Udacity code is as:
    # if self.head.value == value:
    #     self.head = self.head.next
    #     return
    #
    #
    # Since there is a value, there should be a Next, but I am making this check myself instead
    # Their solution is clearer since a linked list that is not None and that contains a value
    # that is not None, should also contain a next.

    while current.next:
        if current.value == value:

            # Again here I am checking if there is a next on a node that contains a value.
            # should be implied that if you have a value, you should have a Next.
            if current.next:
                current.value = current.next.value
                current.next = current.next.next
            else:
                current.next = None
            return

    # Udacity Code: Good to return error messages
    raise ValueError("Value not found in the list.")

    pass


# Udacity Editor has had issues and do not save the history from previous edits, so we must adapt
# and manually add the changes at every update.


def pop(self):
    """ Return the first node's value and remove it from the list. """
    if self.head is None:
        return None

    current = self.head
    self.head = self.head.next

    return current.value


def size(self):
    """ Return the size or length of the linked list. """
    listSize = 0
    current = self.head
    while current:
        listSize += 1
        current = current.next

    return listSize


def to_list(self):
    arrayToReturn = []
    current = self.head
    while current:
        arrayToReturn.append(current.value)
        current = current.next
    return arrayToReturn


# I had issues creating the insert one, I did not exactly know how to think of a way in a list vs
# an Array, but the fact is that indexing is the same and could be done just by saving and iterating
# Like they did in the following solution:
def insert(self, value, pos):
    """ Insert value at pos position in the list. If pos is larger than the
        length of the list, append to the end of the list. """
    # If the list is empty
    if self.head is None:
        self.head = Node(value)
        return

    if pos == 0:
        self.prepend(value)
        return

    index = 0
    node = self.head
    while node.next and index <= pos:
        if (pos - 1) == index:
            new_node = Node(value)
            new_node.next = node.next
            node.next = new_node
            return

        index += 1
        node = node.next
    else:
        self.append(value)


LinkedList.to_list = to_list
LinkedList.size = size
LinkedList.pop = pop
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