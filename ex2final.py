class node:
    def __init__(self):
        self.value = None
        self.next = None

class SLL:
    def __init__(self):
        self.head = node()
        self.size = 0

    def InsertAt(self, value, pos):
        t = node()
        t.value = value

        if (self.size == 0 and pos == 0):
            self.head = t
            self.size += 1
            return True

        elif (pos == 0):
            t.next = self.head
            self.head = t
            self.size += 1
            return True

        elif (pos <= self.size and self.size != 0):
            temp = self.head
            for i in range (pos - 1):
                temp = temp.next
            t.next = temp.next
            temp.next = t
            self.size += 1
            return True

        else:
            print("Invalid insertion")

    def DeleteAt(self, pos):
        if (pos <= self.size and self.size != 0):
            temp = self.head
            for i in range (pos - 1):
                temp = temp.next
            temp.next = temp.next.next
            self.size -= 1

        else:
            print("Empty list")

    def PrintAt(self, pos):
        if (pos <= self.size and self.size != 0):
            temp = self.head
            for i in range (pos - 1):
                temp = temp.next
            print(temp.value)

        else:
            print("Data not found")

    def Print(self):
        temp = self.head
        for i in range (self.size - 1):
            print(temp.value)
            temp = temp.next

Playlist_1 = SLL()

while True:
    print("1.Create a playlist\n2.Insert a new song\n3.Delete a song\n4.Select a song\n5.Display playlist\n6.Exit")
    opt = int(input("Choose an option (1 - 6): "))

    match opt:
        case 1:
            limit = int(input("Enter no. of songs: "))
            for i in range (0, limit):
                song = input("Enter song name: ")
                flag = Playlist_1.InsertAt(song, i)
                if (flag):
                    print("Song added successfully")
                   
        case 2:
            pos = int(input("Enter position: "))
            song = input("Enter song name: ")
            Playlist_1.InsertAt(song, pos - 1)

        case 3:
            pos = int(input("Enter position: "))
            Playlist_1.DeleteAt(pos - 1)

        case 4:
            pos = int(input("Enter position: "))
            Playlist_1.PrintAt(pos - 1)

        case 5:
            Playlist_1.Print()

        case 6:
            break
           
        case _:
            print("Choose a valid option")

