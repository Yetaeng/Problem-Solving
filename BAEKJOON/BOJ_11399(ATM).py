n = int(input())
time_to_withdraw = list(map(int, input().split()))

time_to_withdraw.sort()

result = []
for i in range(n):
    result.append(sum(time_to_withdraw[0:i+1]))

print(sum(result))

# 리스트를 오름차순으로 정렬시킨 후, 자신보다 작은 인덱스의 값들을 모두 더했을 때 최소가 된다.
# 그런 다음 슬라이싱을 이용하여 1번째까지, 2번째까지 ... 마지막까지의 합을 각각 구한 뒤
# 그 합들을 최종적으로 더해주면 정답이 나옴!
