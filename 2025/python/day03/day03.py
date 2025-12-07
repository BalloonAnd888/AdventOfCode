def p1():
    inputs = []
    with open("input.txt", 'r') as file:
        for line in file:
            inputs.append(list(map(int, line.strip())))
    
    sum = 0

    for x in inputs:
        temp = 0

        for i in range(len(x)):
            for j in range(i + 1, len(x)):
                val = int(str(x[i])+str(x[j]))
                if val > temp:
                    temp = val

        sum += temp

    print("Part 1 answer:", sum)

def p2():
    inputs = []
    with open("input.txt", 'r') as file:
        for line in file:
            inputs.append(list(map(int, line.strip())))
    
    sum = 0

    for x in inputs:
        l = 0
        temp = ""
        window = 12 

        while window > 0:
            diff = window - 1
            end = len(x) - diff
            search = x[l : end]
            best = max(search)
            index = search.index(best)
            temp += str(best)
            
            l += index + 1
            window -= 1
        
        sum += int(temp)

    print("Part 2 answer:", sum)

if __name__ == '__main__':
    p1()
    p2()
    