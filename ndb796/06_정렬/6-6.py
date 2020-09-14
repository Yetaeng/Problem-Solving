# 계수 정렬 ( O(N+K) )

array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

# 만약 array의 최대값이 5라면 0부터 5까지 카운트를 할 수 있는 6개의 빈 리스트를 만든다.
count = [0] * (max(array) + 1)

for i in range(len(array)):  # array의 데이터들을 모두 확인하기 위해 범위를 len(array)라고 해줌
    # array리스트의 첫번째 데이터는 7이므로 count리스트의 인덱스 7에 해당하는 곳에 1을 증가시킴.
    count[array[i]] += 1

for i in range(len(count)):
    for j in range(count[i]):  # count리스트에 저장된 카운트 수 만큼 차례로 출력하면 오름차순 정렬이 된다.
        print(i, end='')


# 데이터의 크기 범위가 제한되어 정수 형태로 표현할 수 있을 때만 사용 가능
# 최소와 최대 데이터의 차이가 1,000,000을 넘지 않고, 동일한 값의 데이터가 많을 때 효과적
