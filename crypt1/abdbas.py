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
    product = pp1 + pp2

    results = [pp1, int(str(pp2).strip('0')), product]
    for j in range(3):
        for i in range(len(str(results[0]))):
            temp = int(str(results[0])[i])
            if temp not in results:
                results.append(temp)
        del results[0]
    return results


print(multiply([3, 7, 1, 6, 4]))