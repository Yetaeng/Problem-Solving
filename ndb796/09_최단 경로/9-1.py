import sys

input = sys.stdin.readline
INF = int(1e9)

# 노드의 개수, 간선의 개수 입력받기
n, m = map(int, input().split())

# 시작 노드 번호 입력받기
start = int(input())

# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 만들기
# (노드의 번호를 인덱스로 하여 바로 리스트에 접근하기 위해 노드의 개수 + 1로 크기 할당)
gragh = [[] for i in range(n+1)]

# 방문한 적이 있는지 체크할 리스트 만들기
visited = [False] * (n+1)

# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n+1)

# 모든 간선 정보 입력받기
for _ in range(m):
    # a번 노드에서 b번 노드로 가는 비용이 c이다.
    a, b, c = map(int, input().split())
    gragh[a].append((b, c))

# 방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드의 번호를 반환하는 함수


def get_smallest_node():
    min_value = INF  # 최단 거리
    index = 0  # 가장 최단 거리가 짧은 노드
    for i in range(1, n+1):
        # 최단 거리 테이블에서 i번째 노드의 최단 거리가 최단 거리보다 작고, 방문하지 않은 노드라면
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

# 다익스트라 알고리즘


def dijkstra(start):
    # 시작 노드에 대해서 초기화
    distance[start] = 0
    visited[start] = True
    # 시작 노드 부터 연결된 간선정보 가져옴 (gragh : 2차원)
    # j에는 위에서 입력받은 b(j[0])와 c(j[1])가 전달됨
    for j in gragh[start]:
        # j[0]까지의 최단 거리는 j[1]이다.
        distance[j[0]] = j[1]
        # 시작 노드를 제외한 전체 n-1개의 노드에 대해 반복
        for i in range(n-1):
            # 현재 최단 거리가 가장 짧은 노드를 꺼내서 방문처리
            now = get_smallest_node()
            visited[now] = True
            # 현재 노드와 연결된 다른 노드를 확인
            for j in gragh[now]:
                cost = distance[now] + j[1]
                # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
                if cost < distance[j[0]]:
                    distance[j[0]] = cost


dijkstra(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(n+1):
    # 도달할 수 없는 경우
    if distance[i] == INF:
        print("INFINITY")
    # 도달할 수 있는 경우, 거리 출력
    else:
        print(distance[i])
