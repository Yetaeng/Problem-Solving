A = int(input())
B = int(input())
temp = B
for i in range(3): # i를 3번 반복해라(종료값이 3이면 0,1,2로 3번 반복)
  print(i)
  print(A * (temp % 10)) # temp 값을 10으로 나눈 나머지 값은 입력 값 B의 일의자리를 의미
  temp = temp // 10 # temp 값을 10으로 나눈 몫을 temp에 새롭게 넣음
print(A*B)