import time
start_time = time.time()

h = int(input())
count = 0

# h=3 일때, 0, 1, 2만 검사하게되므로 h+1로 범위를 지정해야함. 그래야 3시도 검사
for i in range(h+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count += 1

print(count)



end_time = time.time()
print("time :", end_time-start_time) #time : 1.9006304740905762

# 1초 단위로 검사해도 전체 탐색할 데이터는 86,400가지 밖에 되지 않음. 이럴 경우 1초씩 증가시켜 모든 데이터를 탐색시켜봐도 됨\
# 즉 완전 탐색을 해도 된다. 확인할 데이터의 전체 개수가 100만 개 이하일 때 가능