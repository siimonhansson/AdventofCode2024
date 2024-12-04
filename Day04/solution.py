def partOne():
    with open('./input.txt', 'r') as f:
        lines = f.readlines()

    lines = [l.replace('\n', '') for l in lines]
    return findXmas(lines)

def partTwo():
    with open('./input.txt', 'r') as f:
        lines = f.readlines()

    lines = [l.replace('\n', '') for l in lines]
    return findMASpattern(lines)

def findXmas(input) -> int:
    height = len(input)
    width = len(input[0])
    count = 0

    directions = [(0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1)]

    def isPosValid(x: int,y: int) -> bool:
        return 0 <= x < height and 0 <= y < width

    for i in range(height):
        for n in range(width):
            if input[i][n] == "X":
                for dx, dy in directions: # Try all directions
                    currentPos = [(i,n)]
                    found = True
                    x,y = i,n

                    for l in "MAS":
                        x,y = x + dx, y + dy
                        if not isPosValid(x, y) or input[x][y] != l:
                            found = False
                            break

                        currentPos.append((x,y))

                    if found:
                        count += 1

    return count

def findMASpattern(input) -> int:
    height = len(input)
    width = len(input[0])
    count = 0

    key = {"M", "S"}

    def checkForCross(row, col) -> bool:
        return {input[row - 1][col - 1], input[row + 1][col + 1]} == key and {input[row - 1][col + 1], input[row + 1][col - 1]} == key

    for row in range(1, height - 1):
        for col in range(1, width - 1):
            if input[row][col] == 'A': # Start check from center
                if checkForCross(row, col):
                    count += 1

    return count

print(partOne())
print(partTwo())