from math import gcd


def solution(w, h):
    total = w * h
    gcd_num = gcd(w, h)
    answer = total - (w + h - gcd_num)
    return answer

# 전체 사각형 개수 - {(w - 최대공약수) + (h - 최대공약수) + 최대 공약수}
# = 전체 사각형 개수 - (w + h - 최대공약수)
