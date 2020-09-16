n = int(input())

arr = []
for i in range(n):
    input_data = input().split()
    arr.append(input_data[0], int(input_data[1]))

arr = sorted(arr, key=lambda student: student[1])  # 정렬 조건이니까! 정렬시킬때 람다식으로 주자!

for student in arr:
    print(student[0], end='')


# lambda 식에 student는... 보충 공부 필요!
