def solution(participant, completion):
    completion.append("z"*20)
    p_sort = sorted(participant)
    c_sort = sorted(completion)
    for p, c in zip(p_sort, c_sort):
        if p != c:
            return p

# zip�Լ� : ������ ������ ��� ���� ���� ������ �ڷ����� �����ִ� ����
# 1�� �ڷ����� 1��° ���� 2�� �ڷ����� 1��° ���� ������