from collections import defaultdict, deque

def p1():
    rules = defaultdict(list)
    updates = []
    res = 0

    with open("input.txt", 'r') as file:
        for line in file:
            if "," in line:
                updates.append(line.strip().split(","))
            else:
                key = line.strip().split("|")
                if "" in key:
                    continue
                rules[key[0]].append(key[1])

    def isOrderValid(update, rules):
        position = {page: i for i, page in enumerate(update)}
    
        for page_x in rules:
            for page_y in rules[page_x]:
                if page_x in position and page_y in position:
                    if position[page_x] > position[page_y]:
                        return False
        return True

    for update in updates:
        if isOrderValid(update, rules):
            res += int(update[(len(update) - 1) // 2])

    print("Part 1 answer: ", res)

def p2():
    rules = defaultdict(list)
    updates = []
    res = 0

    with open("input.txt", 'r') as file:
        for line in file:
            if "," in line:
                updates.append(line.strip().split(","))
            else:
                key = line.strip().split("|")
                if "" in key:
                    continue
                rules[key[0]].append(key[1])
    
    def isOrderValid(update, rules):
        position = {page: i for i, page in enumerate(update)}
    
        for page_x in rules:
            for page_y in rules[page_x]:
                if page_x in position and page_y in position:
                    if position[page_x] > position[page_y]:
                        return False
        return True
    

    


    print("Part 2 answer: ", res)

if __name__ == '__main__':
    p1()
    p2()