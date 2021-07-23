from node import Node


class SingleLinkedList:
    """Create a Single Linked List """

    def __init__(self):
        """Initialize a single linked list"""

        self.head = None
        self.tail = None
        self.size = 0

    def append(self, data):
        """Add a new node to the end of the list"""

        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def size(self):
        """Return the size of the list"""

        return str(self.size)

    def iter(self):
        """Iterate over the list"""

        current = self.head
        while current:
            yield current
            current = current.next

    def delete(self, data):
        """Delete a node from the list"""

        current = self.head
        previous = None
        found = False
        while current and found is False:
            if current.data == data:
                found = True
            else:
                previous = current
                current = current.next
        if current is None:
            raise ValueError("Data not in list")
        if previous is None:
            self.head = current.next
        else:
            previous.next = current.next
        self.size -= 1

    def search(self, data):
        """Search for a node in the list"""

        current = self.head
        found = False
        while current and found is False:
            if current.data == data:
                print(f'Data {data} was found')
                found = True
            else:
                current = current.next
        if current is None:
            raise ValueError("Data not in list")
        return current

    def clear(self):
        """Clear the list"""
        self.head = None
        self.tail = None
        self.size = 0


if __name__ == '__main__':

    sll = SingleLinkedList()
    sll.append(1)
    sll.append('hey')
    sll.append(3.14)
    sll.append('Hola')
    current = sll.tail

    for node in sll.iter():
        print(node.data)

    print(sll.size)
    sll.search('hey').data
    sll.search('545').data
