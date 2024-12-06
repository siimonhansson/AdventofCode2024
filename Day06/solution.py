def parseMap(input):

    mapGrid = [list(row) for row in input.strip().split('\n')]
    startPos = None
    for row in range(len(mapGrid)):
        for col in range(len(mapGrid[row])):
            if mapGrid[row][col] == '^':
                startPos = (col,row)
                break
        if startPos:
            break
    print("Map parsed!")
    return mapGrid, startPos

def isPosValid(pos, mapGrid):
    col, row = pos
    return 0 <= row < len(mapGrid) and 0 <= col < len(mapGrid[0])

def patrol(input):
    mapGrid, pos = parseMap(input)
    visitedCoords = set()
    visitedCoords.add(pos)
    direction = (0, -1)

    while True:
        col, row = pos
        dirCol, dirRow = direction
        nextPos = (col + dirCol, row + dirRow)

        if isPosValid(nextPos, mapGrid) and mapGrid[nextPos[1]][nextPos[0]] != '#':
            pos = nextPos
            if pos not in visitedCoords:
                visitedCoords.add(pos)
        else:
            newX, newY = direction
            direction = (-newY, newX)

        if not isPosValid(nextPos, mapGrid):
            break

    return len(visitedCoords)

def partOne():
    with open('./input.txt', 'r') as f:
        input =  f.read()

    return patrol(input)

def findLoops(input):
    mapGrid, pos = parseMap(input)
    loopOptions = set()

    for row in range(len(mapGrid)):
        for col in range(len(mapGrid[row])):
            if mapGrid[row][col] == '.':
                tempGrid = [x[:] for x in mapGrid] # Apparently mapGrid.copy() only creates a shallow copy...
                tempGrid[row][col] = '#'

                result, path = patrolUntilLoopOrExit(tempGrid, pos)
                if result == "LOOP":
                    loopOptions.add((col,row))

    return len(loopOptions)


def patrolUntilLoopOrExit(mapGrid, startPos):
    direction = (0, -1)
    pos = startPos
    storedStates = set()
    path = []

    while True:
        currentState = (pos, direction)
        path.append(currentState)

        if currentState in storedStates: # Loop found
            loopStart = path.index(currentState)
            return "LOOP", path[loopStart:]
        storedStates.add(currentState)

        col, row = pos
        dirCol, dirRow = direction
        nextPos = (col + dirCol, row + dirRow)

        if isPosValid(nextPos, mapGrid) and mapGrid[nextPos[1]][nextPos[0]] != '#':
            pos = nextPos
        else:
            newX, newY = direction
            direction = (-newY, newX)

        if not isPosValid(nextPos, mapGrid):
            return "EXIT", path

def partTwo():
    with open('./input.txt', 'r') as f:
        input =  f.read()

    return findLoops(input)


# This solution is slow and messy, but in my defense it 1) works and 2) I wanted to solve it ASAP to not waste too much flex time.
# Might revisit tomorrow.
print("Part One: " + str(partOne()))
print("Part Two: " + str(partTwo()))
