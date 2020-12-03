from collections import deque

# 도시의 개수, 도로의 개수, 거리 정보, 출발 도시의 번호
n, m, k, x = map(int, input().split())
graph = [[] for _ in range(m+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)  # a번 도로에서 b번 도로로 이동 가능

# 모든 도시에 대한 최단 거리 초기화 <- 자기 자신으로 가는 최단 거리는 0이므로 -1로 초기화해줌
distance = [-1] * (n+1)
distance[x] = 0  # x는 출발 도시의 번호인데, x의 최단 거리가 0이 됨

q = deque([x])
while q:
    now = q.popleft()
    for next in graph[now]:
        # next 도시에 대한 최단 거리가 초기화(-1) 상태일 때
        if distance[next] == -1:
            distance[next] = distance[now] + 1
            q.append(next)

check = False
for i in range(1, n+1):
    if distance[i] == k:
        print(i)
        check = True

if check == False:
    print(-1)

# 내가 처음 생각했던 방식은 연결된 도로를 따라 가면서 k일 떄 까지만 검사하려고 했는데,
# 이게 아니라 모든 도시에 대하여 최단 거리를 일단 구해고 그 거리가 k인 것을 출력하는 흐름이 맞다,,,
# check를 생각해내는 것도 나에겐 무리였다,,,ㅠ
