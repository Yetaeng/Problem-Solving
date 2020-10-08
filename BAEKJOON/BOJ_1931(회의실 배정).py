import sys

input = sys.stdin.readline
n = int(input())

meetings = []
for i in range(n):
    start, end = map(int, input().split())
    meetings.append((start, end))

# meetings리스트를 정렬할껀데, end(종료시각기준)으로 오름차순 정렬한다.
# 시작시간이 같은 회의에 대해서는 종료시간이 작은걸 선택하면 되므로!
meetings = sorted(meetings, key=lambda time: (time[1], time[0]))
# 어떤 블로그에는 시작시각, 종료시각 각각 정렬해줘야 올바른 그리디 탐색을 할 수 있다고 했는데, 첫번째 정렬 후, 다시 다른 기준으로 정렬하면 처음 정렬된 리스트를 기준으로 하는게 아니던데 왜 해줘야하는거지?

count = 0
temp = 0
for time in meetings:
    if temp <= time[0]:
        count += 1
        temp = time[1]

print(count)

# 정렬을 한 후에, 그 다음 시작할 회의의 시작 시각이 이전 회의이 종료 시각보다 큰 걸 고르면 됐는데,, 이부분이 왜이렇게 구현이 안됐지ㅠ
# 일단은 예제만 보고 <=가 아닌 1보다 큰 걸 고르려고 했다.
# 그리고 큰 걸 골랐으면 바로 카운트하면 됐는데, 또 다른 상황에서 카운트를 하려고 했다.

# min_end = min(time)[1]
# for i in range(n):
#   if min_end <= time[i][1]
#     temp_end = time[i][1]
#   if time[i][0] == temp_end + 1:
#

# for time in meetings:
#   temp_end = time[1]
#   if temp_end+1 == time[0]:
