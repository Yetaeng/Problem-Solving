# 순차 탐색


def sequential_search(n, target, array):
    for i in range(n):
        if array[i] == target:
            return i+1


input_data = input().split()  # 생성할 원소 개수 입력하고, 찾을 문자열 입력
n = int(input_data[0])
target = input_data[1]

array = input().split()

print(sequential_search(n, target, array))
