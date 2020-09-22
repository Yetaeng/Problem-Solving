import sys  # 사실 필요 없음

INF = int(1e9)

# 전체 회사의 개수 n, 경로의 개수 m
n, m = map(int, input().split())
company = [[INF] * (n+1) for i in range(n+1)]

# 간선 정보
for _ in range(m):
    # 연결된 두 회사의 번호
    a, b = map(int, input().split())
    # 각 회사는 1만큼의 시간으로 이동(양방향)
    company[a][b] = 1
    company[b][a] = 1

# 최종 목표 회사 x, 중간에 들릴 회사 k
x, k = map(int, input().split())

# 자기 자신은 시간이 0
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            company[a][b] = 0

# 1번에서 K까지의 최소값과 K번에서 X까지의 최솟값을 더함
for temp in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            company[a][b] = min(company[a][b], company[a]
                                [temp]+company[temp][b])

result = company[1][k] + company[k][x]

# 비교를 ==로 해서 계속 2000000000이 나왔던 것! result가 무한보다 크거나 같다고 해야함
if result >= INF:
    print('-1')
else:
    print(result)
