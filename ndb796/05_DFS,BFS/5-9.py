# BFS 예제
from collections import deque

# BFS 메서드 정의
def bfs(graph, start, visited):
    # 큐 구현을 위해 deque 라이브러리 사용
    # 시작 노드를 원소로 갖고 있는 큐를 생성한다.
    queue = deque([start]) # deque(iterable, [, maxlen]) -> 초기화 함수. iterable을 인자로 건내면 이를 deque화 시켜줌
    
    # 현재 노드를 방문 처리
    visited[start] = True

    # 큐가 빌 때까지 반복
    # 반복문은 queue에 원소가 다 없어질때까지 알아서 돌다가 멈춘다.
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        print(v, end='')
        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

# 각 노드가 연결된 정보를 리스트 자료형으로 표현
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# 각 노드가 방문된 정보를 리스트 자료형으로 표현
visited = [False] * 9

# 정의된 BFS 함수 호출
bfs(graph, 1, visited)

## 각 노드의 연결 정보를 작성하고, 모든 노드의 방문 표시를 false로 초기화한다.
## 함수 호출
### start가 1이므로 1을 원소로 갖고 있는 큐를 생성한다.
### 노드 1을 방문처리한다
### 큐에서 원소 하나를 꺼내는데 이때 1이 꺼내어짐
### 꺼내진 원소(v)와 연결된 원소들(graph[v])을 차례로 방문 처리가 안되어있는지 확인하며 큐에 삽입한다. 그리고 삽입된 원소들을 방문처리한다.