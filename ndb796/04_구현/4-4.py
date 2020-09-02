import time
start_time = time.time()

# 맵의 크기 입력받기
N, M = map(int, input().split())
# 캐릭터의 좌표(a, b)와 바라보는 방향(d) 입력받기
x, y, direction = map(int, input().split())

# 방문 위치를 표시하기 위한 맵을 생성하여 0으로 초기화
visited = [[0]*M for _ in range(N)]
# 현재 방문한 좌표를 1로 처리
visited[x][y] = 1

# 전체 맵 정보 입력받기
array = []
for i in range(N):
    # array라는 리스트에 리스트 형식으로 추가함으로써 2차원 배열이 형성됨
    array.append(list(map(int, input().split())))

# 방향 정의
# dx, dy를 세로로 묶으면 북, 동, 남, 서의 좌표!
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회전시키는 함수
def turn_left():
    global direction
    # 북:0, 동:1, 남:2, 서:3
    direction -= 1
    # 현재가 북쪽이라면 왼쪽으로 돌렸을 때 서쪽이고, direction이 -1이됨
    # direction은 0부터 3까지의 숫자만 허용되니까 3으로 다시 초기화해줌
    if direction == -1:
        direction = 3

# 시뮬레이션 시작
count = 1
turn_time = 0
while True:
    turn_left()
    # 회전하고나서 그 방향으로 좌표 이동
    nx = x + dx[direction] #1
    ny = y + dy[direction] #0
    
    # 회전한 이후 정면에 가보지 않은 칸이 존재하고, 육지인 경우 이동
    if visited[nx][ny] == 0 and array[nx][ny] == 0:
        visited[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
    else:
        # 회전만 수행
        turn_time += 1
    # 네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        # 뒤로 좌표 이동
        nx = x - dx[direction]
        ny = y - dy[direction]
        # 뒤로 갈 수 있다면 이동
        if array[nx][ny] == 0:
            x = nx
            y = ny
        # 뒤가 바다일 때
        else:
            break
        turn_time = 0

print(count)

end_time = time.time()
print("time :", end_time-start_time) #time : 10.72976565361023