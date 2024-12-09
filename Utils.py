def getInputLines():
    with open('./input.txt', 'r') as f:
        return f.readlines()

def getInput():
    with open('./input.txt', 'r') as f:
        return f.read()

def concatenate(a, b) -> int:
    return int(str(a) + str(b))