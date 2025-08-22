class node:
    def __init__(self):
        self.value = None
        self.next = None

class stack:
    def __init__(self):
        self.head = node()
        self.size = 0

    def push(self, value):
        t = node()
        t.value = value
        t.next = self.head
        self.head = t
        self.size += 1
        return True

    def pop(self):
        if(self.size == 0):
            print("Empty book stack")
            return None
        temp = self.head
        self.head = self.head.next
        book = temp.value
        del(temp)
        return book

    def peek(self):
        if(self.size == 0):
            print("Empty book stack")
            return None
        return self.head.value

    def display(self):
        if(self.size == 0):
            print("Empty book stack")
            return None
        temp = self.head
        for i in range (self.size):
            print(temp.value)
            temp = temp.next
            
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
