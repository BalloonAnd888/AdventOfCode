def p1():
    reports = []
    safe = 0

    with open("input.txt", 'r') as file:
        for line in file:
            reports.append(list(map(int, line.strip().split())))

    for r in reports:
        a, b, *rest = r
        isSafe = True
        for c in rest:
            if not ((a < b < c or a > b > c) and 1 <= abs(a-b) <= 3 and 1 <= abs(b-c) <= 3):
                isSafe = False
                break
            a, b = b, c
        
        if isSafe:
            safe += 1

    print("Part 1 answer: ", safe)

def p2():
    reports = []
    safe = 0

    with open("input.txt", 'r') as file:
        for line in file:
            reports.append(list(map(int, line.strip().split())))

    for r in reports:
        a, b, *rest = r
        isSafe = True
        for c in rest:
            if not ((a < b < c or a > b > c) and 1 <= abs(a-b) <= 3 and 1 <= abs(b-c) <= 3):
                isSafe = False
                break
            a, b = b, c
        
        if isSafe:
            safe += 1
        else:
            for i in range(len(r)):
                modified = r[:i] + r[i+1:]
                a, b, *m = modified
                isSafe = True

                for c in m:
                    if not ((a < b < c or a > b > c) and 1 <= abs(a-b) <= 3 and 1 <= abs(b-c) <= 3):
                        isSafe = False
                        break
                    a, b = b, c
            
                if isSafe:
                    safe += 1
                    break

    print("Part 2 answer: ", safe)

if __name__ == '__main__':
    p1()
    p2()
    