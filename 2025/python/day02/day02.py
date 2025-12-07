def p1():
    inputs = []
    with open("input.txt", 'r') as file:
        for line in file:
            line = line.split(",")
            for x in line:
                inputs.append(x.split("-"))
    
    idSum = 0

    for s, e in inputs:
        for x in range(int(s), int(e) + 1):
            if len(str(x)) % 2 != 0:
                continue

            m = len(str(x)) // 2
            num = str(x)

            if (num[:m] == num[m:]):
                idSum += x
            
    print("Part 1 answer:", idSum)

def p2():
    inputs = []
    with open("input.txt", 'r') as file:
        for line in file:
            line = line.split(",")
            for x in line:
                inputs.append(x.split("-"))
    
    idSum = 0

    for s, e in inputs:
        for x in range(int(s), int(e) + 1):
            num_str = str(x)
            length = len(num_str)
            
            for k in range(1, (length // 2) + 1):
                if length % k == 0:
                    pattern = num_str[:k]
                    multiplier = length // k
                    
                    if pattern * multiplier == num_str:
                        idSum += x
                        break 

    print("Part 2 answer:", idSum)

if __name__ == '__main__':
    p1()
    p2()
