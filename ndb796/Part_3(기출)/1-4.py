n = int(input())
data = list(map(int, input().split()))
data.sort()

target = 1
for i in data:
    if target < i:
        break
    else:
        target += i

print(target)

# 감도 못잡은 문제
