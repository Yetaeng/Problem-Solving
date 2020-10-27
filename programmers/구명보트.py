from collections import deque


def solution(people, limit):
    people.sort()
    cnt = 0

    left_idx = 0
    right_idx = len(people)-1
    while left_idx <= right_idx:
        if people[left_idx] + people[right_idx] <= limit:
            cnt += 1
            left_idx += 1
            right_idx -= 1
        else:
            cnt += 1
            right_idx -= 1

    answer = cnt
    return answer
