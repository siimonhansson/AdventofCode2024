import Utils

def parseMap(input):
    return [list(line.strip()) for line in input.strip().split('\n')]

def findAntennas(grid):
    frequencies = {}
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] not in '.':
                freq = grid[row][col]
                if freq not in frequencies:
                    frequencies[freq] = []
                frequencies[freq].append((col, row))
    return frequencies

def findAntinodes(grid, antennas):
    h = len(grid)
    w = len(grid[0])
    antinodes = set()

    print(antennas)
    for freq, positions in antennas.items():
        for i in range(len(positions)):
            for j in range(i + 1, len(positions)):
                ant1 = positions[i]
                ant2 = positions[j]

                antinodePoints = findAntinodePoints(ant1, ant2)

                for col, row in antinodePoints:
                    if 0 <= col < w and 0 <= row < h: # Make sure antinode is inside grid
                        antinodes.add((col, row))

    return len(antinodes)

def findAntinodePoints(ant1, ant2):
    x1,y1 = ant1
    x2,y2 = ant2

    distX = x2 - x1
    distY = y2 - y1

    dist = ((distX ** 2 + distY ** 2) ** 0.5) # Good ol' Pythagora to find Euclidean distance

    if dist != 0: # Only calculate unit vectors if needed. Otherwise, return empty array
        unitDistX = distX / dist
        unitDistY = distY / dist
    else:
        return []

    # Find antinodes in opposite dir of antenna 1
    antinode1x = int(round(x1 - unitDistX * dist))
    antinode1y = int(round(y1 - unitDistY * dist))

    # Find antinodes in same dir as antenna 2
    antinode2x = int(round(x2 + unitDistX * dist))
    antinode2y = int(round(y2 + unitDistY * dist))

    return [(antinode1x, antinode1y), (antinode2x, antinode2y)]

def partOne():
    grid = parseMap(Utils.getInput())
    antennas = findAntennas(grid)
    return findAntinodes(grid, antennas)


def findAntinodes2(grid, antennas):
    h = len(grid)
    w = len(grid[0])
    antinodes = set()

    for freq, positions in antennas.items():
        for row in range(h):
            for col in range(w):
                point = (col, row)
                for i in range(len(positions)):
                    for j in range(i + 1, len(positions)):
                        if isCollinear(positions[i], positions[j], point):
                            antinodes.add(point)
                            break
        for pos in positions: # Convert antennas to antinodes
            antinodes.add(pos)

    return len(antinodes)

def isCollinear(p1, p2, p3):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    return (y2 - y1) * (x3 - x2) == (y3 - y2) * (x2 - x1)

def partTwo():
    grid = parseMap(Utils.getInput())
    antennas = findAntennas(grid)
    return findAntinodes2(grid, antennas)


# This is by far and a way definitely not the intended way to solve this lol
print(partOne())
print(partTwo())
