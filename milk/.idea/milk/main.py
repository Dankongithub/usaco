"""
ID: corbin.1
LANG: PYTHON3
TASK: milk
"""


# input

fin = open("milk.in", "r")
totMilk, numFarmers = fin.readline().strip().split(" ")
milkNeeded = int(totMilk)
numFarmers = int(numFarmers)
farmers = []

for x in range(numFarmers):
    toappend = fin.readline().strip().split(" ")
    for x in range(2):
        toappend[x] = int(toappend[x])
    farmers.append(toappend)

fin.close()

amountSpent = 0
milkBought = 0

farmers.sort()
print(farmers)

# Buy loop
while milkBought < milkNeeded:
    amountSpent += farmers[0][0]
    milkBought += 1
    farmers[0][1] -= 1
    if farmers[0][1] == 0:
        farmers.remove(farmers[0])

fout = open("milk.out", "w")
fout.writelines(str(amountSpent) + "\n")
