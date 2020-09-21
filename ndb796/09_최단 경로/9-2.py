import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())
graph = [[] for i in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


def dijkstra(start):
    # 현재 가장 가까운 노드를 저장하기 위한 리스트
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정한 뒤, 큐에 삽입
    # 우선순위 큐에 (거리:0, 노드:1)의 정보를 가지는 객체를 넣는 것
    heapq.heappush(q, (0, start))
    distance[start] = 0
    # 큐가 비어있지 않는 동안
    while q:
        # 가장 최단 거리가 짧은 노드의 정보 꺼내기
        # 우선순위 큐를 이용하므로 그냥 꺼내기만하면, 그게 가장 짧은 거리를 가진 노드임
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드일 떄
        if distance[now] < dist:
            continue

        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        # now를 노드 1이라고 한다면, graph[1]은 (2, 2), (3, 5), (4, 1)을 차례대로 i에 넘김
        for i in graph[now]:
            # 현재 여기서 dist는 노드 1의 최단거리이므로 0임(즉, 큐에 들어있는 거리 정보)
            cost = dist + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

# distance는 최단거리테이블로 나중에 정답을 출력할 때 사용되는 리스트이고, dist는 큐에 삽입된 노드의 최단거리를 저장해놓는 변수이다.


dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])
