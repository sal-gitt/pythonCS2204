class node:
    def __init__(self):
        self.coeff = None
        self.exp = None
        self.next = None

class SLL:
    def __init__(self):
        self.head = node()
        self.size = 0

    def InsertAt(self, coeff, exp, pos = None):
        t = node()
        t.coeff = coeff
        t.exp = exp

        if (pos == None):
            pos = self.size

        if (pos == 0):
            t.next = self.head
            self.head = t
            self.size += 1
            return True

        elif (pos <= self.size):
            temp = self.head
            for i in range (pos - 1):
                temp = temp.next
            t.next = temp.next
            temp.next = t
            self.size += 1
            return True

def polyn_add(buffer, limit):
    for i in range (limit - 1):
        max_value = max(buffer[i].size, buffer[i+1].size)
        if (buffer[i].size == max_value):
            temp = buffer[i]
            buffer[i] = buffer[i+1]
            buffer[i+1] = temp
        else:
            temp = buffer[i+1]
            buffer[i+1] = buffer[i]
            buffer[i] = temp

        temp1 = buffer[i]
        temp2 = buffer[i+1]    
        for i in range (max_value):
            if (temp1.next is not None):
                if (temp1.exp > temp2.exp):
                    temp2.InsertAt(temp2.coeff, temp2.exp, i)
                elif (temp2.exp > temp1.exp):
                    pos = 0
                    while (temp2.next is not None and temp2.exp > temp1.exp):
                        temp2 = temp2.next
                        pos += 1
                    if (temp2.exp == temp1.exp):
                        temp2.coeff += temp1.coeff
                    else:
                        temp2.InsertAt(temp2.coeff, temp2.exp, pos)
                else:
                    temp2.coeff += temp1.coeff
                temp1 = temp1.next
                temp2 = temp2.next
        
limit = int(input("Enter no. of expressions: "))
buffer = []
coefficients = []
exponents = []
operators = ['+', '-']
for i in range (limit):
    buffer.append(SLL())
    eqn = input("Enter expression: ")
    flag = 0
    for char in eqn:
        if (char.isalpha()):
            flag = 1
            continue
        if (flag != 1):
            coefficients.append(char)
        elif (flag == 1):
            if(char == '^'):
                continue
            if (char.isdigit()):
                exponents.append(char)
        if (char in operators):
            if (char == '-'):
                sign = 1
            if (eqn.index(char) != 0):
                if (sign == 1):
                    coeff = -(int("".join(coefficients)))
                else:
                    coeff = int("".join(coefficients))
                if not exponents:
                    exp = 0
                else:
                    exp = int("".join(exponents))
                coefficients.clear()
                exponents.clear()
                buffer[i].InsertAt(coeff, exp)
            else:
                continue
polyn_add(buffer, limit)

temp = buffer[limit - 1]
for i in range (buffer[limit - 1].size):
    print (f"{temp.coeff}x^{temp.exp}")
    temp = temp.next