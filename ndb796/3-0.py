import time
start_time = time.time()

# 배열의 크기 N, 숫자가 더해지는 횟수 M, 연속해서 더할 수 있는 수 K를 공백으로 구분하여 입력받기
N, M, K = map(int, input().split(" "))
# N개의 자연수를 공백으로 구분하여 입력받기
num = list(map(int, input().split(" ")))
lst = []
count = 0

# 입력받은 수를 내림차순으로 정렬하기
num.sort(reverse=True)

# count가 M이 될 때 까지만 반복문 수행
while(count < M):
    # 가장 큰 수가 중복일 때
    if num[0] == num[1]:
        # K번 만큼 0번째 인덱스에 있는 수를 리스트에 넣음
        for i in range(K):
            lst.append(num[0])
            count += 1
        # K번 만큼 1번째 인덱스에 있는 수를 리스트에 넣음
        for j in range(K):
            lst.append(num[1])
            count += 1
    # 가장 큰 수가 1개 일 때
    else:
        # K번 만큼 0번째 인덱스에 있는 가장 큰 수를 리스트에 넣음
        for i in range(K):
            lst.append(num[0])
            count += 1
        # 그 다음 큰 수를 한 번만 리스트에 넣음
        lst.append(num[1])
        count += 1

# 최종 답안 출력
print(sum(lst))

# 수행 시간 측정
end_time = time.time()
print("time :", end_time-start_time) # 8.09801435470581