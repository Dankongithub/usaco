def rotate90(mtrx):
    n = len(mtrx)
    mtrx.reverse()
    for row in range(n):
        for column in range(row):
            mtrx[row][column], mtrx[column][row] = mtrx[column][row], mtrx[row][column]
    return mtrx


def rotate180(matrix):
    n = len(matrix)
    matrix.reverse()
    for i in range(n):
        matrix[i].reverse()
    return matrix


def rotate270(matrix):
    grid_to_return = rotate90(rotate180(matrix))
    return grid_to_return


def fix_directions(matrix, direction):
    if direction == "up":
        rotate90(matrix)
    elif direction == "down":
        rotate270(matrix)
    elif direction == "left":
        rotate180(matrix)
    return matrix


def unfix_directions(matrix, direction):
    if direction == "up":
        rotate270(matrix)
    elif direction == "down":
        rotate90(matrix)
    elif direction == "left":
        rotate180(matrix)
    return matrix


def print_matrix(mtrx):
    adfasf = 0
    for sfasdf in mtrx:
        if adfasf != 0:
            print("")
        print(*sfasdf, end="")
        adfasf += 1


def move(matrix, direction):
    n = len(matrix)
    matrix = fix_directions(matrix, direction)
    for j in range(n):
        matrix[j] = [item for item in matrix[j] if item != 0]
        for l in range(-1, -len(matrix[j]), -1):
            if matrix[j][l] == matrix[j][l - 1]:
                matrix[j][l - 1] = matrix[j][l - 1] * 2
                del matrix[j][l]
                matrix[j].insert(0, 0)
        while len(matrix[j]) < n:
            matrix[j].insert(0, 0)
    matrix = unfix_directions(matrix, direction)

    return matrix


case = int(input())
for x in range(case):
    board = []
    dimensions, way = input().split()

    dimensions = int(dimensions)

    for i in range(dimensions):
        board.append([int(thing) for thing in input().split()])

    print(f"Case #{x + 1}:")
    print_matrix(move(board, way))
    print("")
