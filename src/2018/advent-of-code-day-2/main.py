import re

boxIDList = [line.rstrip("\n") for line in open("input.txt", "r")]
cntPair = 0
cntTriple = 0

for id in boxIDList:
    sortedId = ''.join(sorted(id))
    if (re.search(r"(?:^|(.)(?!\1))(.)\2(?!\2)", sortedId)): cntPair += 1
    if (re.search(r"(?:^|(.)(?!\1))(.)\2\2(?!\2)", sortedId)): cntTriple += 1

print(cntPair * cntTriple)