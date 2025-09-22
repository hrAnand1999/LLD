from observer import Observer
from observable import Observable

def main():
    book = Observable()
    torch = Observable()

    user1 = Observer('User 1')
    user2 = Observer('User 2')
    user3 = Observer('User 3')

    book.addObserver(user1)
    book.addObserver(user2)
    book.addObserver(user3)

    torch.addObserver(user1)
    torch.addObserver(user2)

    book.setData("Book is available")

    torch.setData("Torch is available")

if __name__ == "__main__":
    main()

