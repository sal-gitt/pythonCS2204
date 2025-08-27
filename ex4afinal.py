class queue:
    def __init__(self):
        self.capacity = 0
        self.queue = []
        self.front = 0
        self.rear = -1
        self.size = 0
        
    def enqueue(self, car):
        if self.size == self.capacity:
            print("Car parking is full")
            return None
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = car
        self.size += 1
        return True
    
    def dequeue(self):
        if self.size == 0:
            print("Car parking is empty")
            return None
        car = self.queue[self.front]
        self.queue[self.front] = None
        self.front += 1
        self.size -= 1
        return car

    def display(self):
        if self.size == 0:
            print("Car parking is empty")
            return None
        for i in range(self.size):
            index = (self.front + i) % self.capacity
            print(f"{self.queue[index]}")

Parking_1 = queue()

while True:
    print("1.Create a new parking\n2.Park new cars\n3.Unpark first car\n4.Display all parked cars\n5.Exit")
    opt = int(input("Choose an option (1 - 5): "))

    match opt:
        case 1:
            size = int(input("Enter parking size: "))
            Parking_1.capacity = size
            Parking_1.queue = [None] * Parking_1.capacity

        case 2:
            limit = int(input("Enter no. of cars: "))
            if (limit > Parking_1.capacity):
                print("Parking capacity exceeded, please try with a lower car count")
                continue
            for _ in range (limit):
                car = input("Enter car name: ")
                flag = Parking_1.enqueue(car)
                if (flag):
                    print("Car parked successfully")

        case 3:
             print(Parking_1.dequeue())

        case 4:
            Parking_1.display()

        case 5:
            break
           
        case _:
            print("Choose a valid option")
