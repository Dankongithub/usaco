"""
ID: corbin.1
LANG: PYTHON3
TASK: palsquare
"""

def checkPalindrome(str):
    if str == str[::-1]:
        return True
    else:
        return False

# Why did I spend so much time on this when i didnt even use it bruh
#def turnBase10(num, base):
#    total = 0
#    letters = [1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
#    for x in range(len(num)):
#        if type(num[-1 - x]) == str:
#            if x >= 1:
#                total += (base ** x) * (letters.index(num[-1 - x], 9, 18) + 1)
#            else:
#                total += letters.index(num[-1 - x], 9, 18) + 1
#
#        else:
#            if x >= 1:
#                total += (base ** x) * (num[-1 - x])
#            else:
#                total += num[-1 - x]
#    return total

def turnBaseB(num, base):
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


# Didn't use this either
#def countUp(num, base):
#    for x in range(20):
#        num.insert(0, 0)
#    letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
#    for i in range(len(num)):
#        if num[-1 - i] == base - 1:
#            num[-1 - i] = 0
#        else:
#            num[-1 - i] += 1
#            break
#    if base > 10:
#        for j in range(len(num)):
#            if num[j] >= 10:
#                num[j] = letters[num[j] - 10]
#    for x in range(len(num)):
#        if num[0] == 0:
#            num.remove(num[0])
#        else:
#            pass


    return num

file = open("palsquare.in", "r")
base = int(file.readline().strip())
file.close()

output = []
for x in range(1, 301):

    x2 = str(x ** 2)
    x = str(x)
    xSquared = []
    for j in range(len(x2)):
        xSquared.append(int(x2[j]))


    y = []
    for i in range(len(x)):
        y.append(int(x[i]))


    baseB = turnBaseB(y, base)
    baseBSquared = turnBaseB(xSquared, base)
    tocheck = ''.join(map(str, baseBSquared))
    if checkPalindrome(tocheck) == True:
        output.append([baseB, baseBSquared])

file = open("palsquare.out", "w")
for x in range(len(output)):
    file.writelines(' '.join(map(str, output[x])) + "\n")

