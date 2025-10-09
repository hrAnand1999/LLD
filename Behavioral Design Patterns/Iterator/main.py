from LinkedList import LinkedList


if __name__ == "__main__":
    l1 = LinkedList([1,2,3,4,5])
    iterator = l1.get_iterator()
    while iterator.has_next():
        print(iterator.next())