input_data = input().split(' ')
A = int(input_data[0])
B = int(input_data[1])

if A > B:
    print(">")
elif A < B:
    print("<")
else: 
    print("==")


---
# else A == B: 라고해서 컴파일 에러 났었음.