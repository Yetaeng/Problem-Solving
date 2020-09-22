INF = int(1e9)

n = int(input())
m = int(input())
# 최단 거리 정보를 저장할 2차원 리스트를 만들고, INF로 초기화
graph = [[INF] * (n+1) for _ in range(n+1)]

# 자기 자신에서 자기 자신으로 가는 비용을 0으로 초기화
# 그래프 왼쪽 위에서, 오른쪽 아래로 내려가는 대각선을 0으로 초기화
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

# 각 간선에 대한 정보 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c

# 점화식에 따라 플로이드 워셜 알고리즘
# a에서 b로 갈 때의 거리와, a에서 k를 거쳐 b로 가는 거리를 비교해 짧은 것을 가져옴
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

# 결과 출력
for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b] == INF:
            print('INFINITY', end=' ')
        else:
            print(graph[a][b], end=' ')
    print()
