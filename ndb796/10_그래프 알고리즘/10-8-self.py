def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n, m = map(int, input().split())
parent = [0] * (n+1)

for i in range(0, n+1):
    parent[i] = i

distances = []
for _ in range(m):
    a, b, fee = map(int, input().split())
    distances.append((fee, a, b))

distances.sort()

result = []
for distance in distances:
    fee, a, b = distance
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result.append(fee)

print(sum(result)-max(result))

# 답안에서는 last라는, 최소 신장 트리에 포함되는 간선 중에서 가장 비용이 큰 간선을 저장할 변수를 만들었다.
# 이미 간선을 비용순으로 정렬해놨으니까 마지막에 저장되는 cost가 가장 크다!

# result, last = 0, 0
# for distance in distances:
#     fee, a, b = distance
#     if find_parent(parent, a) != find_parent(parent, b):
#         union_parent(parent, a, b)
#         result += fee
#         last = fee
# print(result - last)
