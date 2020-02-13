N = int(input()) # N에 6을 입력하면

for i in range(1, N+1): # i에는 1부터 6까지 할당된다. 
  for j in range(0, i): # j에는 0부터 5까지 할당된다.
    print("*", end='')
    # end에 빈 문자열을 지정하면 다음 번 출력이 바로 뒤에 오게 됨
  print() # 첫번째 for문 안에서 실행되는 것
