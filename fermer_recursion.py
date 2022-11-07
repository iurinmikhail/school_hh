# import pytest
import random
# import sys
# sys.setrecursionlimit(10000)
matrix = [[random.randint(0, 1) for _ in range(2, 100)] for _ in range(2, 100)]
# n, m, matrix = 3, 1,  [[1, 0, 1]]
# matrix1 = [
# n, m, matrix = 2, 2, [[0, 1], [1, 0]]
#     ]
# matrix = [[int(i) for i in j] for j in matrix1]
n, m, = len(matrix[0]), len(matrix)

# n, m = [int(i) for i in input().split()]
# matrix = [[int(i) for i in input().split()] for _ in range(m)]

def get_count(matrix, m, n):
    count = 2
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 1:
                get_color(i, j, count)
                count += 1
    region_size = []
    region_effectivity = []
    for c in range(2, count):
        top = 0
        bottom = 0
        left = 0
        right = 0
        good = 0
        square = 0
        flag = True
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == c:
                    if flag:
                        top = i
                        bottom = i
                        left = j
                        right = j
                        flag = False
                    else:
                        top = min(i, top)
                        bottom = max(i, bottom)
                        left = min(j, left)
                        right = max(j, right)
        square = (bottom - top + 1) * (right - left + 1)

        for i in range(top, bottom + 1):
            for j in range(left, right + 1):
                if matrix[i][j] > 0:
                    good += 1

        region_size.append(square)
        region_effectivity.append(int(good*100000 / square))
    return [region_size, region_effectivity]


def get_color(y, x, count):
    matrix[y][x] = count
    for i in range(max(0, y-1), min(y+1, m-1)+1):
        for j in range(max(0, x-1), min(x+1, n-1)+1):
            if matrix[i][j] == 1:
                get_color(i, j, count)

regions = get_count(matrix, m, n)
max_effectivity = 0
max_size = 0
for i in range(len(regions[0])):
    effect = regions[1][i]
    size = regions[0][i]
    if effect >= max_effectivity and size > 1:
        max_effectivity = effect
for i in range(len(regions[0])):
    effect = regions[1][i]
    size = regions[0][i]
    if effect == max_effectivity and size >= max_size and size > 1:
        max_size = size
print(max_size)




