from itertools import combinations

n, m = map(int, input().split())
house, chicken = [], []

for r in range(n):
    data = list(map(int, input().split()))
    for c in range(n):
        if data[c] == 1:
            house.append((r, c))
        elif data[c] == 2:
            chicken.append((r, c))

candidates = list(combinations(chicken, m))


def get_sum(candidates):
    result = 0
    for hx, hy in house:
        temp = 1e9
        # 조합으로 뽑은 치킨집의 좌표
        for cx, cy in candidate:
            temp = min(temp, abs(hx-cx) + abs(hy-cy))
        # 가장 가까운 치킨 거리 더하기
        result += temp
    return result


result = 1e9
for candidate in candidates:
    result = min(result, get_sum(candidate))

print(result)
