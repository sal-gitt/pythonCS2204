class stack:
    def __init__(self):
        self.stack = []

    def push(self, book):
        self.stack.append(book)
        return True

    def pop(self):
        if len(self.stack) == 0:
            print("Empty Book Stack")
        return self.stack.pop()

    def peek(self):
        if len(self.stack) == 0:
            print("Empty Book Stack")
        return self.stack[-1]

    def display(self):
        if len(self.stack) == 0:
            print("Empty Book Stack")
        for book in reversed(self.stack):
            print(f"- {book}")


Library_1 = stack()

while True:
    print("\n1. Create a library\n2. Insert a new book\n3. Remove latest addition\n4. View latest addition\n5. Display library\n6. Exit")
    opt = int(input("Choose an option (1 - 6): "))

    match opt:
        case 1:
            limit = int(input("Enter no. of books: "))
            for i in range(limit):
                book = input("Enter book name: ")
                flag = Library_1.push(book)
                if flag:
                    print("Book placed successfully")

        case 2:
            book = input("Enter book name: ")
            flag = Library_1.push(book)
            if flag:
                print("Book placed successfully")

        case 3:
            print(Library_1.pop())

        case 4:
            print(Library_1.peek())

        case 5:
            Library_1.display()

        case 6:
            break

        case _:
            print("Choose a valid option")
