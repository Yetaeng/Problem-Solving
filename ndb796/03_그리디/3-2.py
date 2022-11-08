import time
start_time = time.time()

n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

# 가장 큰 수가 더해지는 횟수 계산
count = int(m / (k+1)) * k
count += m % (k+1)

result = 0
result += (count) * first
result += (m-count) * second

print(result)

end_time = time.time()
print("time :", end_time-start_time) # 8.029955863952637

# 나는 가장 큰 수가 중복될 수도 있다고 생각하여 코드를 짰는데, 책의 답안 예시는 주어진 입력 예시만 고려하였다. 즉, 가장 큰 수 1개와 두 번째로 큰 수 1개를 사용했다.
# 또한 M의 크기가 100억 이상처럼 커지면 시간 초과 판정을 받을 수도 있다고 하여, 가장 큰 수가 더해지는 횟수를 따로 구해야 했다.
# 그래서 문제를 효율적으로 해결하기 위해서는 가장 먼저 반복되는 수열에 대해서 파악해야 한다고 한다.