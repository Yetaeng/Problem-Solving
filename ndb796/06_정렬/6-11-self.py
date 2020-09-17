n = int(input())

arr = []
for i in range(n):
    input_data = input().split()
    # input_data[0], int(input_data[1]를 괄호로 묶어서 한개로 처리해줘야함! 안그러면 append에는 인자가 하나들어가야하므로 2개가 들어갔다는 에러가 뜸
    arr.append((input_data[0], int(input_data[1])))

arr = sorted(arr, key=lambda student: student[1])  # 정렬 조건이니까! 정렬시킬때 람다식으로 주자!
# arr을 정렬할껀데, student를 매개변수로 설정해서 student의 두번째 요소를 기준으로 정렬하는 키를 만들꺼야

for student in arr:
    print(student[0], end=' ')

# lambda 식에 student는... 보충 공부 필요!
