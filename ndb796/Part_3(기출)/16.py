# [DFS/BFS] 연구소
from itertools import Combination
from collections import deque

# 세로 n, 가로 m
n, m = map(int, input().split())

# 연구소 데이터 입력 받기
lab = []
for _ in range(n):
    lab.append(map(int, input().split()))

# 바이러스 퍼뜨리는 함수


def virus(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False

    if lab[x+1][y] == 0:
        lab[x+1][y] = 2
        virus(x+1, y)
    if lab[x-1][y] == 0:
        lab[x-1][y] = 2
        virus(x-1, y)
    if lab[x][y+1] == 0:
        lab[x][y+1] = 2
        virus(x, y+1)
    if lab[x][y-1] == 0:
        lab[x][y-1] = 2
        virus(x, y-1)
    return True


# 벽을 세울 수 있는(빈 칸인) 위치 찾기
wall_q = []
for i in range(n):
    for j in range(m):
        if lab[i][j] == 0:
            wall_q.append((i, j))

# 벽 3개 선택하기
wall_candidate = deque(combinations(wall_q, 3))
while wall_candidate:
    w = wall_candidate.popleft()
    # 벽 만듬
    for i in range(3):
        x, y = w[i]
        lab[x][y] = 1

    # 바이러스 퍼뜨리기
    for i in range(n):
        for j in range(m):
            if lab[i][j] == 2:
                virus(i, j)

    # 안전 지역 갯수 구하기
    count = 0
    result = []
    for i in range(n):
        for j in range(m):
            if lab[i][j] == 0:
                count += 1

    cp_lab = lab

    result.append(count)
    print(max(result))

    break
