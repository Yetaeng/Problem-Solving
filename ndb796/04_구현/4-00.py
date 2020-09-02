import time
start_time = time.time()

N = int(input())
h, m, s = N, 60, 60
cnt = 0

for i in range(N):
  for j in range(m):
    for k in range(s):
      if '3' in str(k):
        cnt += 1
    if '3' in str(j):
      cnt += 1
  if '3' in str(i):
    cnt += 1

print(cnt)


end_time = time.time()
print("time :", end_time-start_time)

# 제대로 된 출력이 안됐다.ㅠㅠ