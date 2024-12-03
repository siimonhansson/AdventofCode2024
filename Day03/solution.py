def partOne():
    with open('./input.txt', 'r') as f:
        input = f.read()
        return extractMulInstructions(input)

def partTwo():
    with open('./input.txt', 'r') as f:
        input = f.read()
        return extractMulInstructions(input, True)

def extractMulInstructions(input, enableBonusInstructions = False):
    total = 0
    i = 0
    enabled = True

    while i < len(input) - 3: # -3 since we need at least "mul("
        if enableBonusInstructions:
            if input[i:i + 6] == "don't(":
                i += 6
                if i < len(input) and input[i] == ")":
                    enabled = False
            elif input[i:i + 3] == "do(":
                i += 3
                if i < len(input) and input[i] == ")":
                    enabled = True

        if enabled and input[i:i + 4] == "mul(": # Look for mul(
            i += 4

            numOne = ""
            while i < len(input) and input[i].isdigit():
                numOne += input[i]
                i += 1

            if input[i] == ",": # Make sure number is followed by comma, then skip comma
                i += 1

                numTwo = ""
                while i < len(input) and input[i].isdigit():
                    numTwo += input[i]
                    i += 1

                if input[i] == ")":
                    product = int(numOne) * int(numTwo)
                    total += product

        i += 1

    return total


print(partOne())
print(partTwo())