# 퀵 정렬( 평균 O(NlogN), 최악의 경우는 O(N^2) )

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]


def quick_sort(array):
    if len(array) <= 1:  # 현재 리스트의 데이터 개수가 1개인 경우 퀵 정렬이 끝난다.
        return array

    pivot = array[0]  # 리스트에서 첫 번째 데이터를 피벗으로 정하는 것을 호어 분할 방식이라고 한다.
    tail = array[1:]

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x >= pivot]

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)


pritn(quick_sort(array))
