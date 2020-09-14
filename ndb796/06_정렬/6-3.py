# 삽입 정렬( O(N^2) )

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    for j in range(i+1, 0, -1):
        if array[j-1] > array[j]:
            array[j], array[j-1] = array[j-1], array[j]
        else:
            break

print(array)


# 타겟 인덱스와 이 인덱스의 앞부분 인덱스들과 차례로 비교하여 자리를 찾아간다.
# 자리를 찾다가 자신보다 작은 데이터를 만나면 해당 위치에서 멈춘다.(break)
