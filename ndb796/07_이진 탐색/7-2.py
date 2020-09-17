# 이진 탐색 (재귀 함수 이용)
def binary_search(array, target, start, end):
    if start > end:
        return None

    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] > target:  # 전체 원소는 정수이므로 크기 비교해서 범위 줄여나가기
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid+1, end)


# n : 원소의 개수, targer : 찾고자 하는 문자열
n, target = list(map(int, input().split()))
# 전체 원소
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n-1)
if result == None:
    print('원소가 존재하지 않습니다.')
else:
    # 함수 리턴 값으로 mid + 1이라고 하면 result만 출력해도 됨.
    print(result + 1)
