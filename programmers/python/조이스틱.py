# 정확성 54.5 (3, 4,5, 7, 11 실패)
def solution(name):
    target = list(name)

    result = []
    for i in range(len(target)):
        if ord(target[i]) - ord('A') <= 13:
            result.append(ord(target[i]) - ord('A'))
        else:
            result.append(ord('Z')-ord(target[i])+1)

    num_notA = len(target[1:]) - target[1:].count('A')
    left, right = 0, 0

    for i in name[1:]:  # 오른쪽으로 커서 이동하는 경우
        if i != 'A':
            right += 1
        if right == num_notA:
            break

    for i in name[:0:-1]:  # 왼쪽으로 커서 이동하는 경우
        if i != 'A':
            left += 1
        if left == num_notA:
            break

    answer = sum(result, min(left, right))
    return answer


# 두번쨰 반복문에서 왼쪽 끝에 도달했을 때 오른쪽으로 이동시키는게,, 안된다,,
def solution(name):
    target = list(name)

    result = []
    for i in range(len(target)):
        if ord(target[i]) - ord('A') <= 13:
            result.append(ord(target[i]) - ord('A'))
        else:
            result.append(ord('Z')-ord(target[i])+1)
    print(result)

    cursor = [False]*len(name)
    for i, gap in enumerate(result):
        if gap != 0:
            cursor[i] = True
    print(cursor)
    print('개수', len(cursor))

    num_notA = len(target[1:]) - target[1:].count('A')
    print('바꿔야할 문자열의 수', num_notA)
    print('-------- ')

    current = 0
    while num_notA > 0:
        # 카운트 초기화
        L_position = 0
        R_position = 0
        L_cnt = 0
        R_cnt = 0
        comp = []
        print('check', R_position, L_position)
        # 오른쪽으로 이동하는 경우 카운트
        while 1:
            R_position += 1
            R_cnt += 1
            if cursor[current + R_position] == True:
                comp.append(R_cnt)
                break
        # 왼쪽으로 이동하는 경우 카운트
        while 1:
            L_position -= 1
            L_cnt += 1
            # 왼쪽 끝에 다다르면 오른쪽 끝으로 이동
            if current + L_position < 0:
                L_position = len(cursor) - 1
                current = L_position - current

            if cursor[current + L_position] == True:
                print(current + L_position)
                comp.append(L_cnt)
                break

        current = min(comp)
        cursor[current] = False
        num_notA -= 1
        print('comp', comp)
        print('current', current)
        print('new_cursor', cursor)
        print('-------------------')

    print(solution('ABABAAAAABA'))
