from IterableInterface import IterableInterface
from LinkedListIterator import LinkedListIterator
from IteratorInterface import IteratorInterface

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList(IterableInterface):

    def __init__(self, data_list):
        self.head = None
        prev = None
        for data in data_list:
            node = Node(data)
            if not self.head:
                self.head = node
            if prev:
                prev.next = node
            prev = node


    def get_iterator(self) -> IteratorInterface:
        return LinkedListIterator(self.head)