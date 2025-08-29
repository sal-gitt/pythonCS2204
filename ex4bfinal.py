class node:
    def __init__(self):
        self.value = None
        self.next = None

class queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, car):
        t = node()
        t.value = car
        if self.front == None:
            self.front = self.rear = t
            return True
        self.rear.next = t
        self.rear = t
        return True
        
    def dequeue(self):
        if self.front == None:
            print("Car parking is empty")
            return None
        temp = self.front.value
        self.front.value = None
        self.front = self.front.next
        if self.front == None:
            self.rear = None
        return temp
     
    def peek(self):
        if self.front == None:
            print ("Car parking is empty")
            return None
        return self.front.value
  
    def display(self):
        if self.front == None:
            print("Car parking is empty")
            return None
        current = self.front
        while current:
            print(current.value)
            current = current.next
            
Parking_1 = queue()

while True:
    print("1.Park new cars\n2.Display first car\n3.Unpark first car\n4.Display all parked cars\n5.Exit")
    opt = int(input("Choose an option (1 - 5): "))

    match opt:
        case 1:
            limit = int(input("Enter no. of cars: "))
            for _ in range (limit):
                car = input("Enter car name: ")
                flag = Parking_1.enqueue(car)
                if (flag):
                    print("Car parked successfully")
         
        case 2:
             print(Parking_1.peek())
             
        case 3:
             print(Parking_1.dequeue())

        case 4:
            Parking_1.display()

        case 5:
            break
           
        case _:
            print("Choose a valid option")
