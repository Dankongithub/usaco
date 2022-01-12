"""
ID: corbin.1
LANG: PYTHON3
TASK: namenum
"""


def match(string, number):

    if len(string) != l:
        return False

    for x in range(l):
        current_number = number[x]
        if string[x] in ["A", "B", "C"]:
            if 2 != current_number:
                return False
        elif string[x] in ["D", "E", "F"]:
            if 3 != current_number:
                return False
        elif string[x] in ["G", "H", "I"]:
            if 4 != current_number:
                return False
        elif string[x] in ["J", "K", "L"]:
            if 5 != current_number:
                return False
        elif string[x] in ["M", "N", "O"]:
            if 6 != current_number:
                return False
        elif string[x] in ["P", "R", "S"]:
            if 7 != current_number:
                return False
        elif string[x] in ["T", "U", "V"]:
            if 8 != current_number:
                return False
        else:
            if 9 != current_number:
                return False
    return True

def countup(list):
    for x in range(l):
        if list[-1 - x] < 2:
            list[-1 - x] = list[-1 - x] + 1
            break
        else:
            list[-1 - x] = 0


file = open("namenum.in", "r")
numbers = []
while True:
    char = file.read(1)
    if not char or char == "\n":
        break
    numbers.append(int(char))
file.close()

l = len(numbers)

dictionary = []

file = open("dict.txt", "r")
for line in file:
    line = line.strip()
    if match(line, numbers):
        dictionary.append(line)
file.close()


valid_names = sorted(dictionary)


file = open("namenum.out", "w")
if len(valid_names) == 0:
    file.write("NONE\n")

else:
    for x in valid_names:
        file.write(x + "\n")
file.close()
"""
letters = []
for x in range(l):
    if numbers[x] == 2:
        letters.append(["A", "B", "C"])
    elif numbers[x] == 3:
        letters.append(["D", "E", "F"])
    elif numbers[x] == 4:
        letters.append(["G", "H", "I"])
    elif numbers[x] == 5:
        letters.append(["J", "K", "L"])
    elif numbers[x] == 6:
        letters.append(["M", "N", "O"])
    elif numbers[x] == 7:
        letters.append(["P", "R", "S"])
    elif numbers[x] == 8:
        letters.append(["T", "U", "V"])
    else:
        letters.append(["W", "X", "Y"])


possible_names = []
count = []
for x in range(l):
    count.append(0)

for x in range(3 ** l):
    name = ""

    for j in range(l):
        name = name + letters[j][count[j]]
    countup(count)
    if name in dictionary:
        possible_names.append(name)


possible_names = sorted(possible_names)

file = open("namenum.out", "w")
if len(possible_names) == 0:
    file.write("NONE\n")

else:
    for x in range(len(possible_names)):
        file.write(possible_names[x] + "\n")
file.close()
"""