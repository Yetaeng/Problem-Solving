def solution(arr, k):
    new_arr = [] # 2차원 리스틀 1차원으로 만들어주기 위해 빈 리스트를 생성한다.
    for i in arr:
        new_arr += i
        new_arr.sort()
    return new_arr[k-1] # new_arr은 리스트이므로 ()가 아니라 []로 해줘야지!