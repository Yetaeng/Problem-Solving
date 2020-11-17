def solution(citations):
    citations.sort()
    ci_cnt = 0
    result = []
    for i in citations:
        for j in citations:
            if i <= j:
                ci_cnt += 1
        result.append(ci_cnt)
        ci_cnt = 0

    for i in range(len(citations)):
        if citations[i] == result[i]:
            return citations[i]

# citations 배열을 내림차순으로 정렬해야한다.
# 이는 h번 이상 인용된 논문이 h편 이상이 되는 값은 즉 h의 최대 값을 구하는 거나 마찬가지이기 때문이다.


def solution(citations):
    if sum(citations) == 0:  # citations가 0으로만 이루어졌을 때 0 리턴
        return 0
    else:
        for h in range(max(citations), 0, -1):
            ci_cnt = 0
            for citation in citations:
                if citation >= h:
                    ci_cnt += 1
                if ci_cnt == h:
                    return h
# 참고 https://itholic.github.io/kata-h-index/
