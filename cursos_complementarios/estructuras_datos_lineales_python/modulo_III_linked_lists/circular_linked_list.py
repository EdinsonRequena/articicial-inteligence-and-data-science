from typing import Any
from node import Node


class CircularLinkedList:

    def __init__(self):
        """Inizialite a Circular Linked List"""

        self.head = Node(None, None)
        self.head.next = self.head

    def add(self, data: any) -> Node:
        """Returns a new node"""

        new_node = Node(data, self.head.next)
        self.head.next = new_node
        new_node.next = self.head
        return new_node

    def iter(self):
        """Iterate over the list"""

        current = self.head.next
        while current != self.head:
            yield current
            current = current.next

    def __str__(self) -> str:
        """String representation of the list"""
        return " ".join([str(node) for node in self.iter()])

if __name__ == '__main__':

    cll = CircularLinkedList()
    cll.add(1)
    print(cll.head.next.data)

