# 내 코드
s = input()
s = list(map(int, s))

result = 0
for i in range(0, len(s)-1):
  # for j in range(i+1 , len(s)):
    if s[i] == s[i+1]:
        result += 0
    else:
        result += 1
print(result-1)


# 정답 코드
data = input()
count0 = 0
count1 = 0

if data[0] == '1':
    count0 += 1
else:
    count1 += 1

for i in range(len(data)-1):
    if data[i] != data[i+1]:
        if data[i+1] == '1':
            count0 += 1
        else:
            count1 += 1
print(min(count0, count1))
