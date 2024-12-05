from functools import cmp_to_key


def getParsedInput():
    with open('./input.txt', 'r') as f:
        input =  f.read()

    sections = input.strip().split('\n\n')
    return sections[0].strip().split('\n'), sections[1].strip().split('\n')

# Convert rules list into a dictionary. Each key in the dict represents a number that needs to come before it's entries.
def getRules(rulesList) -> {}:
    rules = {}
    for rule in rulesList:
        before, after = map(int, rule.split('|'))
        if before not in rules:
            rules[before] = set()
        rules[before].add(after)
    return rules

def isCorrectlyOrdered(pages, rules) -> bool:
    length = len(pages)

    for i in range(length):
        for j in range(i + 1, length):
            pageOne, pageTwo = pages[i], pages[j]
            if pageTwo in rules and pageOne in rules[pageTwo]:
                return False

    return True

def convertUpdateListToInt(updateList):
    return [list(map(int, update.strip().split(','))) for update in updateList]

# Eh, it works...
def sortByRules(update, rules):

    # I like this feature :)
    def compare(a: int, b:int) -> int:
        if b in rules[a]:
            return -1
        if a in rules[b]:
            return 1
        return 0

    return sorted(update, key=cmp_to_key(compare))


def solve():
    rulesList, updatesList = getParsedInput()
    rules = getRules(rulesList)
    updates = convertUpdateListToInt(updatesList)
    correctUpdates, incorrectUpdates = [], []

    for update in updates:
        if isCorrectlyOrdered(update, rules):
            correctUpdates.append(update)
        else:
            incorrectUpdates.append(update)

    partOneTotal = 0
    for update in correctUpdates:
        partOneTotal += update[len(update) // 2]

    partTwoTotal = 0
    for update in incorrectUpdates:
        sortedUpdate = sortByRules(update, rules)
        partTwoTotal += sortedUpdate[len(sortedUpdate) // 2]

    return "Part One: " + str(partOneTotal) + "\nPart Two: " + str(partTwoTotal)

print(solve())
