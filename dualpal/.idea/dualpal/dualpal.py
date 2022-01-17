"""
ID: corbin.1
TASK: dualpal
LANG: PYTHON3
"""

def checkPalindrome(str):
    if str == str[::-1]:
        return True
    else:
        return False

def turnBaseB(num, base):

    num = [int(x) for x in str(num)]

    return_value = []
    for x in range(20):
        return_value.insert(0, 0)
    for x in range(len(num)):
        num[x] = str(num[x])
    num = int("".join(num))

    letters = [1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    remainder = num
    next = num
    j = 0
    while next >= base:
        remainder = next%base
        next = next//base
        return_value[-1 - j] = remainder
        j += 1
    return_value[-1 - j] = next

    for x in range(len(return_value)):
        if return_value[0] == 0:
            return_value.remove(return_value[0])
        else:
            pass
    for x in range(len(return_value)):
        if return_value[x] >= 10:
            return_value[x] = letters[return_value[x] - 1]

    return ''.join(map(str, return_value))

fin = open("dualpal.in", "r")
N, S = fin.readline().strip().split(" ")
N = int(N)
S = int(S)
fin.close()
fout = open("dualpal.out", "w")

howManyFound = 0
x = S + 1
while howManyFound < N:

    isDoublePalindrome = []

    for i in range(2, 11):
        baseI = turnBaseB(x, i)

        isPalindrome = checkPalindrome(str(baseI))

        if isPalindrome:
            isDoublePalindrome.append(isPalindrome)

        try:
            if isDoublePalindrome[0] and isDoublePalindrome[1]:
                howManyFound += 1
                print(str(x) + " " + str(baseI) + " " + str(i))
                fout.writelines(str(x) + "\n")
                break
        except:
            pass

    x += 1