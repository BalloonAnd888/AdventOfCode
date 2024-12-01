from collections import Counter

# Part 1
def p1():
    list1, list2 = [], []
    distance = 0
    
    with open("input.txt", 'r') as file:
        for line in file:
            line = line.strip()
            line = line.split()
            list1.append(int(line[0]))
            list2.append(int(line[1]))
    
    list1.sort()
    list2.sort()
    
    for l1, l2 in zip(list1, list2):
        distance += abs(l1 - l2)
        
    print("Part 1 answer: ", distance)

# Part 2 
def p2():
    l, r = [], []
    simScore = 0
    
    with open("input.txt", "r") as file:
        for line in file:
            line = line.strip()
            line = line.split()
            l.append(int(line[0]))
            r.append(int(line[1]))
    
    r = Counter(r)
    
    for x in l:
        simScore += x*r[x]
    
    print("Part 2 answer: ", simScore)

if __name__ == '__main__':
    p1()
    p2()
