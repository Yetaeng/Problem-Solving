s = str(input())
s = list(map(int, s))
s.sort()

result = 0
for i in range(len(s)):
    # 처음엔 1이 아닌 0으로 했다가, 이렇게 되면 1+2=3 > 1*2=2 같은 경우를 못잡음!(정답 참고함)
    if s[i] >= 1 or result >= 1:
        result += s[i]
    else:
        result *= s[i]

print(result)
