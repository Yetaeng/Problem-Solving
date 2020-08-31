import time
start_time = time.time()

n, k = map(int, input().split())
count = 0

while (1):
  if n % k == 0:
    n = n // k
    count += 1
    if n == 1:
      break
  else:
    n -= 1
    count += 1
    if n == 1:
      break

print(count)

end_time = time.time()
print("time :", end_time-start_time) #time : 1.494236707687378