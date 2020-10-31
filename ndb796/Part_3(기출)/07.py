N = list(map(int, input()))
length = len(N)
left = []
right = []

for i in range(length//2):
    left.append(N[i])
for j in range(length//2, length):
    right.append(N[j])


if sum(left) == sum(right):
    print('LUCKY')
else:
    print('READY')
