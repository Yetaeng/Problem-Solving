data = input()
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
            'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

arr1 = [x for x in data if x in alphabet]
arr2 = [y for y in data if y not in alphabet]

arr1.sort()
arr2 = map(int, arr2)

for i in arr1:
    print(i, end="")
print(sum(arr2))


# isalpha()라는게 있네,,, 아래는 정답 코드
# data = input()
# result = []
# value = 0


# for x in data:
#     if x.isalpha():
#         result.append(x)
#     else:
#         value += int(x) # x는 str이니까 int로 변환해서 더해주기

# result.sort()
# if value != 0:
#     result.append(str(value)) # 다시 str로 변화해서 더해줌. 문자열끼리는 더하면 이어서 붙여지니까!

# print(''.join(result))
