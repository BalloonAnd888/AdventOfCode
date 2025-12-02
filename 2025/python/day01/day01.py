def p1():
    inputs = []
    with open("input.txt", "r") as file:
        for line in file:
            line = line.strip()
            inputs.append([line[0], int(line[1:])])

    dial = 50
    password = 0

    for direction, value in inputs:
            if direction == "L":
                dial = (dial - value) % 100
            elif direction == "R":
                dial = (dial + value) % 100
                
            print(f"Move {direction}{value} -> Dial is now {dial}")

            if dial == 0:
                password += 1
    
    print("Part 1 answer:", password)

def p2():
    inputs = []
    with open("input.txt", "r") as file:
        for line in file:
            line = line.strip()
            inputs.append([line[0], int(line[1:])])

    dial = 50
    password = 0

    for direction, value in inputs:
        password += value // 100
        
        remaining_steps = value % 100
        
        for _ in range(remaining_steps):
            if direction == "L":
                dial -= 1
            elif direction == "R":
                dial += 1
            
            dial %= 100
            
            if dial == 0:
                password += 1

    print("Part 2 answer:", password)

if __name__ == '__main__':
    p1()
    p2()
    