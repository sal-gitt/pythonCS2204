res = []
buffer = []
buffer_size = 0
operators = {"(": 0, "/" : 1, "*" : 1, "+" : 2, "-" : 2} 
exp = input("Enter infix expression: ")
for char in exp:
    if char.isalnum():
        res.append(char)
    else:
        if len(buffer) == 0:
            buffer.append(char)
            buffer_size += 1
            continue
        temp1 = operators.get(buffer[-1])
        if operators.get(char) < temp1:
            if char == "(":
                buffer.append(char)
                buffer_size += 1
                marker1 = buffer_size
                continue
            buffer.append(char)
            buffer_size += 1
        elif char == ")":
            res.extend(buffer[-1:marker1])
            buffer_size -= len(buffer[-1:marker1]) + 1
            del buffer[-1:marker1+1]
        else:
            temp2 = operators.get(char) 
            for char in reversed(buffer):
                if operators.get(char) > temp2:
                    marker2 = buffer.index(char)
                    res.extend(buffer[-1:marker2])
                    buffer_size -= len(buffer[-1:marker2]) + 1
                    del buffer[-1:marker2+1]
                    break
            buffer.append(char)
            buffer_size += 1
while len(buffer) != 0:
    for char in reversed(buffer):
        res.append(char)
        buffer.remove(char)
buffer.clear()

print("".join(res))
