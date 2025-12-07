def p1():
    inputs = []
    with open("input.txt", 'r') as file:
        for line in file:
            inputs.append(line.strip())
    
    ranges = []
    ids = []

    for x in range(len(inputs)):
        if inputs[x] == "":
            x += 1
            while x < len(inputs):
                ids.append(int(inputs[x]))
                x += 1
            break
        ranges.append(inputs[x].split("-"))

    ans = 0

    for id in ids:
        for s, e in ranges:
            if id in range(int(s), int(e) + 1):
                ans += 1
                break

    print("Part 1 answer: ", ans)

def p2():
    inputs = []
    with open("input.txt", 'r') as file:
        for line in file:
            inputs.append(line.strip())
    
    ranges = []
    ids = []

    for x in range(len(inputs)):
        if inputs[x] == "":
            x += 1
            while x < len(inputs):
                ids.append(int(inputs[x]))
                x += 1
            break
        ranges.append(inputs[x].split("-"))

    ranges = sorted([[int(item) for item in sublist] for sublist in ranges])

    mergedIntervals = [ranges[0]]

    for i in range(1, len(ranges)):
        currStart, currEnd = ranges[i]
        lastStart, lastEnd = mergedIntervals[-1]

        if currStart <= lastEnd:
            mergedIntervals[-1] = [lastStart, max(currEnd, lastEnd)]
        else:
            mergedIntervals.append([currStart, currEnd])

    ans = 0

    for s, e in mergedIntervals:
        ans += e - s + 1

    print("Part 2 answer: ", ans)

if __name__ == '__main__':
    p1()
    p2()