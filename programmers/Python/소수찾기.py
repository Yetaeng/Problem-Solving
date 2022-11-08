from itertools import permutations


def check_prime(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def solution(numbers):
    # numbers로 만들 수 있는 모든 숫자를 찾는다.
    result = []
    for i in range(1, len(numbers)+1):
        whole_num = list(map(''.join, permutations(numbers, i)))

        # whole_num 중복 제거
        whole_num = list(set(whole_num))
        for j in whole_num:
            j = int(j)

            # 소수 판별
            if check_prime(j):

                # j가 정수형으로 삽입되어야 11과 011를 같은 숫자로 취급할 수 있음
                result.append(j)
    return len(set(result))

# 순열을 사용한 후, 튜플에서 어떻게 값을 꺼내야할지 몰랐다...map함수를 이용해서 ''.join!!!!!
# 풀이를 찾아보니까 에라토스테네스의 체를 이용해서도 푸는 것 같다. 하지만 나는 처음 들었고!
