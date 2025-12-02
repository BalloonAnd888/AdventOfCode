def p1():
    grid = []
    startPos = []
    visited = set()

    with open("input.txt", 'r') as file:
        for line in file:
            grid.append(line.strip())

    print(grid)

    rows = len(grid)
    cols = len(grid[0])

    for x in range(rows):
        for y in range(cols):
            if grid[x][y] == '^':
                startPos.append(x)
                startPos.append(y)
    
    print(startPos)

    directions = ["up", "right", "down", "left"]
    diridx = 0
    visited.add((startPos[0], startPos[1]))

    move = {
        'up': (-1, 0),    # Move up (decrease x)
        'right': (0, 1),  # Move right (increase y)
        'down': (1, 0),   # Move down (increase x)
        'left': (0, -1)   # Move left (decrease y)
    }

    x, y = startPos
    moves = 0

    while True:
        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
            break

        if grid[x][y] == '#':
            diridx = (diridx + 1) % 4
        else:       
            dx, dy = move[directions[diridx]]
            x += dx
            y += dy
            print(x, y)

            if (x,y) not in visited:
                moves += 1
                visited.add((x, y))


    print(moves)



    print("Part 1 answer: ")

def p2():
    print("Part 2 answer: ")

if __name__ == '__main__':
    p1()
    p2()