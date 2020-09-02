import time
start_time = time.time()

positions = list(input())
positions[1] = int(positions[1])
count = 0

# 현재 위치에서 오른쪽으로 2칸 이동할 수 있나?
if ord(positions[0]) < 103:
  ## 그렇다면 2칸 이동해라
  ord(positions[0]) + 2
  ## 위로 한칸 이동할 수 있나?
  if positions[1] > 1:
    ### 그렇다면 카운트를 1 증가시킨다.
    count += 1
  ## 아래로 한칸 이동할 수 있나?
  elif positions[1] < 8:
    ### 그렇다면 카운트를 1 증가시킨다.
    count += 1

# 현재 위치에서 왼쪽으로 2칸 이동할 수 있나?
if ord(positions[0]) > 98:
  ## 그렇다면 2칸 이동해라
  ord(positions[0]) - 2
  ## 위로 한칸 이동할 수 있나?
  if positions[1] > 1:
    ### 그렇다면 카운트를 1 증가시킨다.
    count += 1
  ## 아래로 한칸 이동할 수 있나?
  elif positions[1] < 8:
    ### 그렇다면 카운트를 1 증가시킨다.
    count += 1

# 현재 위치에서 위로 2칸 이동할 수 있나?
if positions[1] > 2:
  ## 그렇다면 이동해라
  positions[1] - 2
  ## 오른쪽으로 한칸 이동할 수 있나?
  if ord(positions[0]) < 104:
    ### 그렇다면 카운트를 1 증가시킨다.
    count += 1
  ## 왼쪽으로 한칸 이동할 수 있나?
  elif ord(positions[0]) > 97: 
    ### 그렇다면 카운트를 1 증가시킨다.
    count += 1

# 현재 위치에서 아래로 2칸 이동할 수 있나?
if positions[1] < 7:
  ## 그렇다면 이동해라
  positions[1] + 2
  ## 오른쪽으로 한칸 이동할 수 있나?
  if ord(positions[0]) < 104:
    ### 그렇다면 카운트를 1 증가시킨다.
    count += 1
  ## 왼쪽으로 한칸 이동할 수 있나?
  elif ord(positions[0]) > 97: 
    ### 그렇다면 카운트를 1 증가시킨다.
    count += 1

print(count)

end_time = time.time()
print("time :", end_time-start_time)

# 출력 결과가 제대로 안나옴! 틀린 코드,,, 다시 풀기,,,
