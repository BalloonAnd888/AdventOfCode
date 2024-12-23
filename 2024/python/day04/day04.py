def p1():
    grid = []
    res = 0

    with open("input.txt", 'r') as file:
        for line in file:
            grid.append(line.strip())

    rows, cols = len(grid), len(grid[0])
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

    for x in range(rows):
        for y in range(cols):
            if grid[x][y] == "X":
                for dx, dy in dirs:
                    found = True
                    nx, ny = x + dx, y + dy
                    for char in "MAS":
                        if nx not in range(rows) or ny not in range(cols) or grid[nx][ny] != char:
                            found = False
                            break
                        nx, ny = nx + dx, ny + dy
                    if found:
                        res += 1
    
    print("Part 1 answer: ", res)

def p2():
    grid = []
    res = 0

    with open("input.txt", 'r') as file:
        for line in file:
            grid.append(line.strip())
    
    def inBounds(x,y):
        return x in range(rows) and y in range(cols)
    
    def doubleMTop(x, y):
        return (inBounds(x+-1,y+-1) and grid[x+-1][y+-1] == "M") and (inBounds(x+-1,y+1) and grid[x+-1][y+1] == "M") and (inBounds(x+1,y+-1) and grid[x+1][y+-1] == "S") and (inBounds(x+1,y+1) and grid[x+1][y+1] == "S")
        
    def doubleSTop(x, y):
        return (inBounds(x+-1,y+-1) and grid[x+-1][y+-1] == "S") and (inBounds(x+-1,y+1) and grid[x+-1][y+1] == "S") and (inBounds(x+1,y+-1) and grid[x+1][y+-1] == "M") and (inBounds(x+1,y+1) and grid[x+1][y+1] == "M")

    def topMS(x, y):
        return (inBounds(x+-1,y+-1) and grid[x+-1][y+-1] == "M") and (inBounds(x+-1,y+1) and grid[x+-1][y+1] == "S") and (inBounds(x+1,y+-1) and grid[x+1][y+-1] == "M") and (inBounds(x+1,y+1) and grid[x+1][y+1] == "S")

    def topSM(x, y):
        return (inBounds(x+-1,y+-1) and grid[x+-1][y+-1] == "S") and (inBounds(x+-1,y+1) and grid[x+-1][y+1] == "M") and (inBounds(x+1,y+-1) and grid[x+1][y+-1] == "S") and (inBounds(x+1,y+1) and grid[x+1][y+1] == "M")

    rows, cols = len(grid), len(grid[0])

    for x in range(rows):
        for y in range(cols):
            if grid[x][y] == "A":
                if (doubleMTop(x, y) or doubleSTop(x, y) or topMS(x, y) or topSM(x, y)):
                    res += 1

    print("Part 2 answer: ", res)

if __name__ == '__main__':
    p1()
    p2()
