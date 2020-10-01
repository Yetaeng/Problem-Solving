n, m = map(int, input().split())
arr = []
result = []
for i in range(m):
    operation, a, b = map(int, input().split())
    arr.append((operation, a, b))

for i in range(m):
    if arr[i][0] == 1:
        if arr[i][1] == arr[i][2]:
            print("YES")
        else:
            print("NO")
    else:
        continue
