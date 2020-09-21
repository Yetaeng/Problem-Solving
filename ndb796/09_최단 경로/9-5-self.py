import heapq
import sys

# 도시 C에 인접한 노드들의 개수와, 그 노드들에 메시지가 전달되는 시간 중 최대값을 구하면 됨!
# 도시 수는 통로의 수와 같거나 작을 것!?

input = sys.stdin.readline
INF = int(1e9)

# 도시의 개수, 통로의 개수, 메시지를 보내고자 하는 도시 city
n, m, city = map(int, input().split())
# 최단 거리 테이블
distance = [INF] * (n+1)
# 통로에 대한 정보를 저장한 2차원 리스트
graph = [[] for i in range(n+1)]
# 통로에 대한 정보 입력받기
for _ in range(m):
    x, y, z = map(int, input().split())
    # 도시 x에서 도시 y로 이어지는 통로가 있는데, 이때 메시지가 전달되는 시간이 z
    graph[x].append((y, z))

start = city


def how_long_message(start):
    q = []
    result = []
    heapq.heappush(q, (0, start))
    for i in graph[start]:
        result.append(i[1])
    return max(result)


print(m, how_long_message(start))


# 출력 결과는 예시대로 잘 나오는데 다른 테스트케이스가 있다면 막힐 삘...?
# 35분 소요
