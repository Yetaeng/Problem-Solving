# DFS 예제
# (현재 노드들의 연결된 정보, 현재 위치, 방문 여부를 표시할 정보)
def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end='')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        # 인접노드를 방문하지 않았다면
        if not visited[i]:
            dfs(graph, i, visited)

# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트, 인접행렬로 표현)
graph = [
    [],
    [2, 3, 8], # 노드 1에 연결된 노드들. 즉 노드2, 3, 8이 노드 1에 연결되어 있다.
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False] * 9

# 정의된 DFS 함수 호출 
dfs(graph, 1, visited)

## 각 노드가 연결된 정보를 표시하고,
## 각 노드들을 아직 방문하지 않았으므로 false로 초기화 시킴
## 함수 호출
### 함수가 호출되면 현재 노드(v)를 방문처리한다. 예를 들어 v=1일때, visited[1]이 true가 되면서 방문처리를 하는 것이다.
### 현재 노드를 출력. 스택에서 노드 1을 꺼내는 것
### 현재 노드와 연결된 다른 노드들을 재귀적으로 방문. 에를 들어 노드 1에는 2, 3, 8이 연결되어 있는데 graph[1]은 [2, 3, 8]이므로
### for문을 이용해 이들을 차례대로 방문 확인함
### 만약에 해당 노드가 방문처리되어 있지 않다면, 즉 visited[2]가 false라면 노드 2에서 dfs 함수를 호출한다.