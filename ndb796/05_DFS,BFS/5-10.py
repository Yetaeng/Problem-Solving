# from collections import deque

n, m = map(int, input().split())

# 2차원 리스트의 맵 정보
graph = []
for i in range(n):
    graph.append(list(map(int, input())))


def dfs(x, y):
    # 주어진 범위를 벗어날 때
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False

    # 현재 노드를 아직 방문하지 않았을 때
    # 근데 왜 여기서 elif를 안하고 if로 할까?
    if graph[x][y] == 0:
        # 현재 노드 방문처리
        graph[x][y] = 1
        # 상, 하, 좌, 우 -> 이 위치들을 재귀호출해야함
        # graph[x-1][y] = 1 이런식으로 말고...
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False


# 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1

print(result)
