def solution(participant, completion):
    completion.append("z"*20)
    p_sort = sorted(participant)
    c_sort = sorted(completion)
    for p, c in zip(p_sort, c_sort):
        if p != c:
            return p

# zip함수 : 동일한 갯수의 요소 값을 갖는 시퀀스 자료형을 묶어주는 역할
# 1번 자료형의 1번째 값과 2번 자료형의 1번째 값을 묶어줌