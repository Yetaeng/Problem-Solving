# n : 화페 종류 수, m : 가치의 합
n, m = map(int, input().split())

value = []
for i in range(n):
    value.append(int(input()))

d = [10001] * (m+1)
d[0] = 0

for i in range(n):
    for j in range(value[i], m+1):  # 나는 시작 값을 1로 줬었다.. 그게 아니고 갖고있는 화폐 단위 첫 값부터!
        d[j] = min(d[j], d[j-value[i]] + 1)

if d[m] == 10001:  # 이 문제의 d리스트는 0부터 계산해야함! (난 m+1로 했었음)
    print(1)
else:
    print(d[m+1])


# 문제만 보고 못풀다가, 문제 해설보고 힌트얻어서 품. 근데 군데군데 틀렸음
