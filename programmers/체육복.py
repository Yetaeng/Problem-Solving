# 그리디
def solution(n, lost, reserve):
    # 도난만 당하거나 여벌만 갖고 있는 학생들
    lost_only = set(lost) - set(reserve)
    reserve_only = set(reserve) - set(lost)

    for i in reserve_only:
        if i-1 in lost_only:
            lost_only.remove(i-1)
        elif i+1 in lost_only:
            lost_only.remove(i+1)

    answer = n - len(lost_only)
    return answer

# 처음에는 3, 4, 5, 7, 11 테스트케이스 실패뜨다가 다음에는 1, 2, 5, 9 런타임에러 떴다
# 시간 너무 오래잡아먹어서 다른사람 풀이(개발개발블로그?)를 참고했다.
# 내가 실수한 2가지 중 하나는 모든 학생들 탐색하려고 했던 것과,
# 다른 하나는 lost, reserve의 값(즉, 숫자가) 자체가 중요한건데 위치에 집중해서 for문을 0부터 n까지 돌리는 것만 생각했다.
