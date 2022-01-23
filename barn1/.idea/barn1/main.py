"""
ID: corbin.1
TASK: barn1
LANG: PYTHON3
"""

def biggestGaps(arr, gapCount):
    gaps = []
    for i in range(len(arr)-1):
        gaps.append(arr[i+1]-arr[i])
    gaps.sort()
    returnValue = []
    for x in range(gapCount):
        returnValue.append(gaps[-x - 1] - 1)
    print(returnValue)
    return returnValue


fin = open("barn1.in", "r")
boards, stalls, cows = fin.readline().split(" ")
boards = int(boards)
stalls = int(stalls)
cows = int(cows)


occupied_stalls = []
for x in range(cows):
    occupied_stalls.append(int(fin.readline().strip()))
occupied_stalls.sort()
fin.close()

if cows > boards:
    out = 0
    gaps = biggestGaps(occupied_stalls, boards - 1)

    for x in range(len(gaps)):
        out += gaps[x]

    print(occupied_stalls)
    fout = open("barn1.out", "w")
    fout.writelines(str(occupied_stalls[-1] - occupied_stalls[0] + 1 - out) + "\n")

else:
    fout = open("barn1.out", "w")
    fout.writelines(str(cows) + "\n")
