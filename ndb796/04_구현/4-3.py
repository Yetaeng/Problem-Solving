input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0]) - ord('a')) + 1 # 이렇게 해야 1열부터 시작

# 나이트가 이동할 수 있는 8가지 방향을 정의한다.
steps = [
    (-2, -1), (-1, -2), (-2, +1), (-1, +2), (+2, -1), (+1, -2), (+2, +1), (+1, +2)
]

result = 0
for step in steps:
    # 이동
    next_row = row + step[0]
    next_column = column + step[1]

    # 이동이 가능한지 여부 확인
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1

print(result)

# 나는 이동하기전 위치가 이동할 수 있는 범위에 있는지 판단한 후 이동시키려고 했는데
# 답안 예시를 보니 이동한 후, 그 좌표가 좌표 평면을 벗어나지 않는다면 이동이 잘 된거로 하여 카운트를 증가시켰다.
# 상하좌우 문제처럼 이동경로를 주고 해야지! 했는데, case1 = [2, 1], case = [1, 2]로 밖에 생각이 나지 않아 써먹을 방법을 못찾았었다..

