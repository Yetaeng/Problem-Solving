import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

n, m, start = map(int, input().split())
distance = [INF] * (n+1)
graph = [[] for i in range(n+1)]

for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    # 아 나는 distance를 만들어두고, 뒤에서 result를 또 만들어서 정답을 구했넵,,
    distance[start] = 0

    # q가 비어있지 않을 동안만 동작해야하는데, 이 처리도 안함!
    while q:
        # 최단 거리가 가장 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(start)

# 도달할 수 있는 노드의 개수
count = 0
# 도달할 수 있는 노드 중에서, 가장 멀리 있는 노드와의 최단 거리
max_distance = 0

for d in distance:
    # 도달할 수 있는 노드인 경우
    if d != INF:
        count += 1
        max_distance = max(max_distance, d)

# 시작 노드는 제외해야 하므로 1을 뺀 count를 출력
print(count-1, max_distance)

# 개선된 다익스트라 알고리즘의 기본 소스에서 마지막만 추가 및 수정하면 해결 가능한 문제!!
