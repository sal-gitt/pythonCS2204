class node:
    def __init__(self):
        self.coeff = None
        self.exp = None
        self.next = None

class SLL:
    def __init__(self):
        self.head = None
        self.size = 0

    def InsertAt(self, coeff, exp):
        t = node()
        t.coeff = coeff
        t.exp = exp

        if self.head is None or self.head.exp < exp:
            t.next = self.head
            self.head = t
        else:
            temp = self.head
            while temp.next is not None and temp.next.exp >= exp:
                temp = temp.next
            t.next = temp.next
            temp.next = t
        self.size += 1

def polyn_add(buffer):
    for i in range(len(buffer) - 1):
        p1 = buffer[i]
        p2 = buffer[i + 1]

        t1 = p1.head
        while t1:
            t2 = p2.head
            found = False
            while t2:
                if t2.exp == t1.exp:
                    t2.coeff += t1.coeff
                    found = True
                    break
                t2 = t2.next
            if not found:
                p2.InsertAt(t1.coeff, t1.exp)
            t1 = t1.next


limit = int(input("Enter number of expressions: "))
buffer = []

for i in range(limit):
    buffer.append(SLL())
    eqn = input(f"Enter expression {i+1}: ")
    eqn = eqn.replace(" ", "").replace("-", "+-")
    terms = eqn.split("+")
    for term in terms:
        if not term:
            continue
        if "x" in term:
            parts = term.split("x")
            coeff = parts[0]
            coeff = int(coeff) if coeff not in ("", "+", "-") else int(coeff + "1")
            exp = int(parts[1][1:]) if "^" in term else 1
        else:
            coeff = int(term)
            exp = 0
        buffer[i].InsertAt(coeff, exp)

polyn_add(buffer)

print("\nResultant Polynomial:")
temp = buffer[-1].head
if temp is None:
    print("0")
else:
    terms = []
    while temp:
        if temp.coeff != 0:
            if temp.exp == 0:
                terms.append(f"{temp.coeff}")
            elif temp.exp == 1:
                terms.append(f"{temp.coeff}x")
            else:
                terms.append(f"{temp.coeff}x^{temp.exp}")
        temp = temp.next
    print(" + ".join(terms).replace("+ -", "- "))
