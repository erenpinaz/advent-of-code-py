# Input
# ==========

freqChangeList = [int(line) for line in open("input.txt", "r").readlines()]

# Part 1
# ==========

freq = 0

for ch in freqChangeList:
    freq += ch

print(freq)

# Part 2
# ==========

currFreq = 0
freqResultList = []

i = 0
while True:
    currFreq += freqChangeList[i]
    if currFreq in freqResultList:
        print(currFreq) 
        break
    freqResultList.append(currFreq)
    i = (i + 1) % len(freqChangeList)