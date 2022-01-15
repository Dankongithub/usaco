import copy


def checkPalindrome(str):
    if str == str[::-1]:
        return True
    else:
        return false

def turnBase10(num, base):
    total = 0
    letters = [1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    for x in range(len(num)):
        if x >= 1:
            print(x)
            total += (x ** base) * (letters.index(num[-1 - x]) + 1)
        else:
            print(str(x) + " based")
            total += letters.index(num[-1 - x]) + 1
    return total

def countUp(num, base):
    for x in range(20):
        num.insert(0, 0)
    letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    for i in range(len(num)):
        if num[-1 - i] == base - 1:
            num[-1 - i] = 0
        else:
            num[-1 - i] += 1
            break
    if base > 10:
        for j in range(len(num)):
            if num[j] >= 10:
                num[j] = letters[num[j] - 10]
    for x in range(len(num)):
        if num[0] == 0:
            num.remove(num[0])
        else:
            pass


    return num

print(turnBase10([1, "A", "A"], 11))



