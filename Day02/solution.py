def partOne():
    safeEntries = 0
    with open('./input.txt', 'r') as f:
        lines = f.readlines()

    lines = [l.replace('\n','') for l in lines]
    for i in range(len(lines)):
        if isIncreasingOrDecreasingByMax([int(num) for num in lines[i].split(" ")]):
            safeEntries += 1

    return safeEntries

def partTwo():
    safeEntries = 0
    with open('./input.txt', 'r') as f:
        lines = f.readlines()

    lines = [l.replace('\n','') for l in lines]
    for i in range(len(lines)):
        if isIncreasingOrDecreasingByMaxWithSkip([int(num) for num in lines[i].split(" ")]):
            safeEntries += 1

    return safeEntries

def isIncreasingOrDecreasingByMaxWithSkip(input):
    if isIncreasingOrDecreasingByMax(input):
        return True

    for i in range(len(input)):
        if isIncreasingOrDecreasingByMax(input, i):
            return True

    return False

def isIncreasingOrDecreasingByMax(input, skipIndex = -1):
    sequence = input.copy()

    if skipIndex >= 0:
        sequence = input[:skipIndex] + input[skipIndex+1:]

    isIncreasing = sequence[1] > sequence[0]

    for i in range(len(sequence) - 1):
        delta = sequence[i + 1] - sequence[i]

        if isIncreasing:
            if delta <= 0 or delta > 3:
                return False
        else:
            if delta >= 0 or delta < -3:
                return False

    return True

print(partOne())
print(partTwo())