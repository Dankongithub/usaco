"""
ID: corbin.1
LANG: PYTHON3
TASK: crypt1
"""
from itertools import product


def get_digit(number, n):
    return number // 10**n % 10


def multiply(abc):
    abc = list(abc)
    for i in range(len(abc)):
        abc[i] = str(abc[i])
    number1 = ""
    for i in range(3):
        number1 = number1 + abc[i]
    number2 = ''
    for i in range(3, 5):
        number2 = number2 + abc[i]
    number1, number2 = int(number1), int(number2)
    pp1 = get_digit(number2, 0) * number1
    pp2 = (get_digit(number2, 1) * number1) * 10
    total = pp1 + pp2

    if pp1 > 999:
        return False
    if pp2//10 > 999:
        return False
    if total > 9999:
        return False
    results = [pp1, pp2//10, total]
    for j in range(3):
        for i in range(len(str(results[0]))):
            temp = int(str(results[0])[i])
            if temp not in results:
                results.append(temp)
        del results[0]
    return results


fin = open('crypt1.in', 'r')
N = int(fin.readline().strip())
nums = fin.readline().strip().split(' ')
for x in range(N):
    nums[x] = int(nums[x])



possible = 0

permutations = list(product(nums, repeat=5))


for x in range(len(permutations)):
    if multiply(permutations[x]) is not False and set(multiply(permutations[x])).issubset(nums):
        possible += 1

fout = open("crypt1.out", "w")
fout.writelines(str(possible) + '\n')
