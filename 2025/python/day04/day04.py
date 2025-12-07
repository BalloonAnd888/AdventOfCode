def p1():
    inputs = []
    with open("input.txt", 'r') as file:
        for line in file:
            inputs.append(list(line.strip()))
    
    print(inputs)

    ans = 0
    dir = [(0,1), (0, -1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]

    for m in range(len(inputs)):
        for n in range(len(inputs[m])):
            if inputs[m][n] == "@":
                counter = 0
                for dx, dy in dir:
                    if m + dx in range(len(inputs)) and n + dy in range(0, len(inputs[m])) and inputs[m + dx][n + dy] == "@":
                        counter += 1
                if counter < 4:
                    ans += 1

    print("Part 1 answer: ", ans)

def p2():
    inputs = []
    with open("input.txt", 'r') as file:
        for line in file:
            inputs.append(list(line.strip()))
    
    print(inputs)

    ans = 0
    dir = [(0,1), (0, -1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    canRemoved = False

    while not canRemoved:
        removed = []
        for m in range(len(inputs)):
            for n in range(len(inputs[m])):
                if inputs[m][n] == "@":
                    counter = 0
                    for dx, dy in dir:
                        if m + dx in range(len(inputs)) and n + dy in range(0, len(inputs[m])) and inputs[m + dx][n + dy] == "@":
                            counter += 1
                    if counter < 4:
                        ans += 1
                        removed.append((m, n))
                
        if removed:
            for m, n in removed:
                inputs[m][n] = "x"
        else:
            canRemoved = True

    print("Part 2 answer: ", ans)

if __name__ == '__main__':
    p1()
    p2()
    