import time
start_time = time.time()

n, m = map(int, input().split())
num = []

# 행의 수대로 입력 받기
for i in range(n):
    # 첫번째 행에 데이터 입력 받기    
    data = list(map(int, input().split()))
    # 그 중에서 가장 작은 수를 num에 저장
    num.append(min(data))

# 저장된 num 에서 최대값 출력
# 최종 답안
print(max(num))

end_time = time.time()
print("time :", end_time-start_time) #time : 14.124173879623413