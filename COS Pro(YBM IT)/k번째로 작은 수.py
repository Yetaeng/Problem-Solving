def solution(arr, k):
    new_arr = [] # 2���� ����Ʋ 1�������� ������ֱ� ���� �� ����Ʈ�� �����Ѵ�.
    for i in arr:
        new_arr += i
        new_arr.sort()
    return new_arr[k-1] # new_arr�� ����Ʈ�̹Ƿ� ()�� �ƴ϶� []�� �������!