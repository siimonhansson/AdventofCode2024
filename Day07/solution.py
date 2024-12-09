def getInputLines():
    with open('./input.txt', 'r') as f:
        return f.readlines()

def parseInputLine(line):
    testValueString,numbersString = line.split(':')
    testValue = int(testValueString)
    numbers = [int(x) for x in numbersString.strip().split()]
    return testValue, numbers

def bruteForceCheck(testValue, numbers):
    operatorsCount = len(numbers) - 1
    for i in range(2 ** operatorsCount): # Give us power-to operator in C# plox
        operators = []
        temp = i
        for _ in range(operatorsCount):
            if temp % 2 == 0:
                operators.append('+')
            else:
                operators.append('*')
            temp //= 2

        if solveExpression(numbers, operators) == testValue:
            return True
    return False

def solveExpression(numbers, operators):
    result = numbers[0]
    for i in range(len(operators)):
        if operators[i] == '+':
            result += numbers[i + 1]
        elif operators[i] == '*':
            result *= numbers[i + 1]
        else:
            result = concatenate(result, numbers[i + 1])
    return result

def partOne():
    input = getInputLines()
    total = 0
    for line in input:
        testValue, numbers = parseInputLine(line.strip())
        if bruteForceCheck(testValue, numbers):
            total += testValue

    return total

def bruteForceCheckTwo(testValue, numbers):
    operatorsCount = len(numbers) - 1
    for i in range(3 ** operatorsCount):
        operators = []
        temp = i
        for _ in range(operatorsCount):
            if temp % 3 == 0:
                operators.append('+')
            elif temp % 3 == 1:
                operators.append('*')
            else:
                operators.append('||')
            temp //= 3

        if solveExpression(numbers, operators) == testValue:
            return True
    return False

def concatenate(a, b):
    return int(str(a) + str(b))

def partTwo():
    input = getInputLines()
    total = 0
    for line in input:
        testValue, numbers = parseInputLine(line.strip())
        if bruteForceCheckTwo(testValue, numbers):
            total += testValue

    return total


print(partOne())
print(partTwo())

