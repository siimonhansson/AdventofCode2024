from collections import Counter


def partOne():
    with open('./input.txt', 'r') as f:
        leftCol, rightCol = splitToColumn(f)

    if len(leftCol) != len(rightCol):
        print("ERROR: Columns not equal size")
        return 0

    leftCol.sort()
    rightCol.sort()

    distance = 0

    for i in range(len(leftCol)):
        distance += abs(leftCol[i] - rightCol[i])

    return distance

def partTwo():
    with open('./input.txt', 'r') as f:
        leftCol, rightCol = splitToColumn(f)

    if len(leftCol) != len(rightCol):
        print("ERROR: Columns not equal size")
        return 0

    leftCol.sort()
    rightCol.sort()

    counter = Counter(rightCol)
    similarity = 0

    for num in leftCol:
        similarity += num * counter.get(num, 0)

    return similarity

def splitToColumn(input):
    leftCol = []
    rightCol = []

    for line in input:
        numbers = line.strip().split('   ')
        if len(numbers) != 2:
            print("WARNING: More than two number on line!")
            continue

        leftCol.append(int(numbers[0]))
        rightCol.append(int(numbers[1]))

    return leftCol, rightCol

result = partOne()
print(result)
result = partTwo()
print(result)
