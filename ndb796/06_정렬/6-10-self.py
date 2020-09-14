n = int(input())
arr = []

for i in range(n):
    data = int(input())
    arr.append(data)

arr = sorted(arr, reverse=True)

for i in arr:
    print(i, end='')
print()
