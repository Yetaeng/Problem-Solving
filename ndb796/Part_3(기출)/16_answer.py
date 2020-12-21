# 세로 n, 가로 m
n, m = map(int, input().split())

# 벽을 설치한 뒤의 맵 리스트
temp = [[0] * m for _ in range(n)]

# 초기 맵 리스트에 연구소 데이터 입력 받기
lab = []
for _ in range(n):
    lab.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def virus(x, y):  # DFS를 이용해 바이러스 퍼뜨리기
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if temp[nx][ny] == 0:
                # 바이러스 배치 후, 재귀적으로 수행
                temp[nx][ny] = 2
                virus(nx, ny)


def get_score():  # 안전 영역 크기 구하기
    score = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                score += 1
    return score


def dfs(count):  # DFS를 이용해 울타리를 설치하면서, 매번 안전 영역의 크기 계산
    global result
    if count == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = lab[i][j]
        # 각 바이러스의 위치에서 전파 진행
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i, j)
        # 안전 영역의 최댓값 계산
        result = max(result, get_score())
        return
    # 빈 공간에 울타리 설치
    for i in range(n):
        for j in range(m):
            if lab[i][j] == 0:
                lab[i][j] = 1
                count += 1
                dfs(count)
                lab[i][j] = 0
                count -= 1


dfs(0)
print(result)


# 멀었다 멀었어,,, 난 왜 이렇게 생각하지 못할까ㅜ
