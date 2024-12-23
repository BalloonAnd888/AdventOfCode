import re

def p1():
    with open("input.txt", 'r') as file:
        memory = file.read().strip()
    
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"

    matches = re.findall(pattern, memory)

    total = sum(int(x) * int(y) for x, y in matches)
    
    print("Part 1 answer: ", total)

def p2():
    print("Part 2 answer: ")

if __name__ == '__main__':
    p1()
    p2()