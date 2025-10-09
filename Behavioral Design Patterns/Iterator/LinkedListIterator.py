from IteratorInterface import IteratorInterface

class LinkedListIterator(IteratorInterface):
    def __init__(self, head):
        self.current = head

    def has_next(self) -> bool:
        return self.current is not None
    
    def next(self):
        if not self.has_next():
            raise StopIteration("No more elements in the linked list.")
        data = self.current.data
        self.current = self.current.next
        return data