## min() 함수 이용
import time
start_time = time.time()

n, m = map(int, input().split())

result = 0
# 한 줄씩 입력받아 확인
for i in range(n):
  data = list(map(int, input().split()))
  # 현재 줄에서 가장 작은 수 찾기
  min_value = min(data)
  # 가장 작은 수들 중에서 가장 큰 수 찾기
  result = max(result, min_value)

print(result)

end_time = time.time()
print("time :", end_time-start_time) #time : 10.849538326263428

#-----------------------
## 2중 반복문 구조 이용
import time
start_time = time.time()

n, m = map(int, input().split())

result = 0
# 한 줄씩 입력받아 확인
for i in range(n):
    data = list(map(int, input().split()))

  # 현재 줄에서 가장 작은 수 찾기
  min_value = 10001
  for a in data:
    min_value = min(min_value, a)

  # 가장 작은 수들 중에서 가장 큰 수 찾기
  result = max(result, min_value)

print(result)

end_time = time.time()
print("time :", end_time-start_time) #time : 17.05822730064392