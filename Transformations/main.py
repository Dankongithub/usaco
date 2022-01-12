"""
ID: corbin.1
LANG: PYTHON3
TASK: transform
"""

import copy


def rotate90(array):
    N = len(array)
    array.reverse()
    for row in range(N):
        for column in range(row):
            array[row][column], array[column][row] = array[column][row], array[row][column]
    return array


def rotate180(array):
    N = len(array)
    array.reverse()
    for i in range(N):
        array[i].reverse()
    return array


def rotate270(array):
    grid_to_return = rotate90(rotate180(array))
    return grid_to_return


def reflection(array):
    N = len(array)
    for i in range(N):
        array[i].reverse()
    return array


def printGrid(array):
    N = len(array)
    for i in range(N):
        print(str(array[i]))


inputStream = open("transform.in", "r")
N = int(int(inputStream.readline()))
grid = []
transformed = []
for i in range(N):
    grid.append(list(inputStream.readline().strip()))
for i in range(N):
    transformed.append(list(inputStream.readline().strip()))
inputStream.close()


rotated90 = rotate90(copy.deepcopy(grid))

rotated180 = rotate180(copy.deepcopy(grid))

rotated270 = rotate270(copy.deepcopy(grid))

reflected = reflection(copy.deepcopy(grid))

reflected90 = rotate90(copy.deepcopy(reflected))

reflected180 = rotate180(copy.deepcopy(reflected))

reflected270 = rotate270(copy.deepcopy(reflected))


transformation = 7
if rotated90 == transformed:
    transformation = 1
elif rotated180 == transformed:
    transformation = 2
elif rotated270 == transformed:
    transformation = 3
elif reflected == transformed:
    transformation = 4
elif reflected90 == transformed or reflected180 == transformed or reflected270 == transformed:
    transformation = 5
elif grid == transformed:
    transformation = 6

file = open("transform.out", "w")
file.write(str(transformation) + "\n")
print(transformation)
file.close()
