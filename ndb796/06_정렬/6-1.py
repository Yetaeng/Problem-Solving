# 선택 정렬( O(N^2) )

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_index = i
    for j in range(i+1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]

print(array)

# 가장 작은 원소를 맨 앞으로 보내는 정렬이다.
# 맨 앞에서부터 가장 작은 원소를 채워 넣기 위한 인덱스(min_index)가 필요하고,
# 비교할 인덱스도 필요하므로 for문을 돌려 비교해준다.
