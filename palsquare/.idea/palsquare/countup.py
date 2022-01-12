def countup(list):
    for x in range(l):
        if list[-1 - x] < 2:
            list[-1 - x] = list[-1 - x] + 1
            break
        else:
            list[-1 - x] = 0