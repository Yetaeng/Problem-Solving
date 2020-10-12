# 내 코드
n, m = map(int, input().split())
data = list(map(int, input().split()))
data.sort()

result = 0
for i in range(n-1):
    for j in range(i+1, n):
        if data[i] != data[j]:
            result += 1
        else:
            continue

print(result)


# 정답 코드
n, m = list(map(int, input().split()))
data = list(map(int, input().split()))
data.sort()

# 1부터 10까지의 무게를 담을 수 있는 리스트
array = [0] * 11
for x in data:
    # 각 무게에 해당하는 볼링공의 개수 카운트
    array[x] += 1

result = 0
for i in range(1, m+1):
    n -= array[i]  # 무게가 i인 볼링공의 개수(A가 선택할 수 있는 개수)제외
    result += array[i]*n
print(result)
