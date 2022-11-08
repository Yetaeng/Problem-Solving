import time
start_time = time.time()

n, k = map(int, input().split())
count = 0

while (1):
  # N이 K로 나누어 떨어진다면, N을 K로 나눈 후 count 1 증가시킨다.
  if n % k == 0:
    n = n // k
    count += 1
    # 그리고 그때 N이 1이 된다면 반복문을 탈출한다.
    if n == 1:
      break
  # N이 K로 나누어 떨어지지 않는다면, N을 1씩 감소시킨다.
  else:
    n -= 1
    count += 1
    if n == 1:
      break

print(count)

end_time = time.time()
print("time :", end_time-start_time) #time : 1.494236707687378

# 나누는 것이 가장 빨리 N을 1로 만들 수 있으므로, 나누어 떨어진다는 가정을 먼저 하였고, 만약 나누어 떨어지지 않는다면 1씩 감소시켜 나누어 떨어질 수 있는 N이 되도록 만들었다.
