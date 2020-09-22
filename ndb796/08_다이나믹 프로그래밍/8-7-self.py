n = int(input())
d = [0] * 1001

d[1] = 1
d[2] = 3

for i in range(3, n+1):
    d[i] = (d[i-1]+2 * d[i-2]) % 796796

print(d[n])

# d[1] = 1
# d[2] = 3
# d[3] = 5
# 이런식으로 DP리스트의 각 인덱스 값을 구해보면 점화식을 쉽게 구할 수 있음!!
