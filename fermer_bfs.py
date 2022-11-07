from collections import deque

# n, m = [int(i) for i in input().split()]
# mat = [[int(i) for i in input().split()] for _ in range(m)]
n, m, mat = 5, 3, [[1, 1, 0, 0, 1],[1, 1, 0, 0, 1],[1, 1, 0, 0, 1]]
# matrix = [[random.randint(0, 1) for _ in range(2, 100)] for _ in range(2, 100)]




row = [-1, -1, -1, 0, 1, 0, 1, 1]
col = [-1, 1, 0, -1, -1, 1, 0, 1]

def isSafe(mat, x, y, processed):
    return (x >= 0 and x < len(processed)) and (y >= 0 and y < len(processed[0])) and \
           mat[x][y] == 1 and not processed[x][y]


def BFS(mat, processed, i, j, count):
    q = deque()
    q.append((i, j))
    processed[i][j] = True
    while q:
        x, y = q.popleft()
        for k in range(len(row)):
            if isSafe(mat, x + row[k], y + col[k], processed):
                mat[x + row[k]][y + col[k]] = count
                processed[x + row[k]][y + col[k]] = True
                q.append((x + row[k], y + col[k]))


def countIslands(mat):

    if not mat or not len(mat):
        return 0


    (M, N) = (len(mat), len(mat[0]))

    processed = [[False for x in range(N)] for y in range(M)]

    island = 2
    for i in range(M):
        for j in range(N):
            if mat[i][j] == 1 and not processed[i][j]:
                mat[i][j] = island
                BFS(mat, processed, i, j, island)
                island = island + 1

    return island


count = countIslands(mat)

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
            if mat[i][j] == c:
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
            if mat[i][j] > 0:
                good += 1

    region_size.append(square)
    region_effectivity.append(int(good*100000 / square))

regions = [region_size, region_effectivity]

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
