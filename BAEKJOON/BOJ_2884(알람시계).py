input_data = input().split(' ')

H = int(input_data[0])*60

M = int(input_data[1])

time = H + M - 45
new_H = time // 60
new_M = time % 60

if new_H < 0:
    new_H = new_H + 24
print(new_H, new_M)