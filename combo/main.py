"""
ID: corbin.1
LANG: PYTHON3
TASK: combo
"""
from itertools import product


def list_int(arr):
    return [int(i) for i in arr]


def closest_numbers(arr):
    for i in range(3):
        to_append = [arr[0] - 2, arr[0] - 1, arr[0], arr[0] + 1, arr[0] + 2]
        for j in range(5):
            if to_append[j] > N:
                to_append[j] = to_append[j] - N
            if to_append[j] <= 0:
                to_append[j] = N + to_append[j]
        arr.append(to_append)
        del arr[0]
    return arr


fin = open("combo.in", "r")
N = int(fin.readline())
combo = closest_numbers(list_int(fin.readline().strip().split(' ')))
combo1 = closest_numbers(list_int(fin.readline().strip().split(' ')))

areCombosTheSame = False
if combo == combo1:
    areCombosTheSame = True

fin.close()

numbers = []
for x in range(1, N + 1):
    numbers.append(x)

combos = list(product(numbers, repeat=3))

numCombos = 0

if areCombosTheSame:
    for x in range(len(combos)):
        if combos[x][0] in combo[0] and combos[x][1] in combo[1] and combos[x][2] in combo[2]:
            numCombos += 1
else:
    for x in range(len(combos)):
        if combos[x][0] in combo[0] and combos[x][1] in combo[1] and combos[x][2] in combo[2]:
            numCombos += 1
            continue
        if combos[x][0] in combo1[0] and combos[x][1] in combo1[1] and combos[x][2] in combo1[2]:
            numCombos += 1

fout = open("combo.out", "w")
fout.writelines(f'{numCombos}\n')
