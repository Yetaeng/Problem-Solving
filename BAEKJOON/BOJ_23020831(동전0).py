n, k = map(int, input().split())
coins = []
result = 0

for i in range(n):
    coins.append(int(input()))

for i in range(n-1, -1, -1):
    if k == 0:
        break
    if coins[i] > k:
        continue
    result += k // coins[i]
    k %= coins[i]

print(result)
