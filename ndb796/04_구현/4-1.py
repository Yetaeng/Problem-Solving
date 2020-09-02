n = int(input())
x, y = 1, 1
plans = input().split()

# L, R, U, D에 따른 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

# 이동 계획을 하나씩 확인
for plan in plans:
    # 이동 후 좌표 구하기
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    # 공간을 벗어나는 경우 무시
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    # 이동 수행
    x, y = nx, ny

print(x, y)

# 나의 풀이와 다르게 확실히 수학적으로 접근한 것 같다. if문의 조건에 공간을 벗어나는 경우를 작성하고, 그때 continue를 실행시키는건 맞았는데
# 나는 너무 일차원적으로 접근하려고 한 것 같다. 처음엔 2차원 배열을 만들어야 하다가 좌표만 나오면 되니까 그냥 단순히 left, right 값만 구하려고 했기 때문인 것 같다.