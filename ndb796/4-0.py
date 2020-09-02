import time
start_time = time.time()

N = int(input())
plan = input().split()
left = 1
right = 1

for i in plan:
  if i == "L" and right != 1:
    right -= 1
  elif i == "R" and right != N:
    right += 1
  elif i == "U" and left != 1:
    left -= 1
  elif i == "D" and left != N:
    left += 1

print('최종', left, right)

end_time = time.time()
print("time :", end_time-start_time) #time : 3.6641509532928467


# for i in plan:
#   if (right == 1 and plan == "L") or (right == N and plan == "R") or (left == 1 and plan == "U") or (left == N and plan == "D"):
#     continue
#   elif i == "L":
#     right -= 1
#     print(left, right)
#   elif i == "R":
#     right += 1
#     print(left, right)
#   elif i == "U":
#     left -= 1
#     print(left, right)
#   else:
#     left += 1
#     print(left, right)

#  처음엔 이런 조건문을 썼는데 정사각형 공간을 벗어나는 움직임이 무시 되지 않았다. 그래서 2, 4가 출력됐다. 왜 if문에서 안걸려졌지?