def solution(number, k):
    arr = list(number)  # 숫자를 리스트로 받음
    stack = []  # 정답을 리턴할 숫자들을 스택에 넣음
    cnt = 0  # 제거한 숫자를 카운트하기 위함
    length = len(arr) - k  # 출력할 문자열의 개수

    stack.append(arr[0])
    for i in range(1, len(arr)):
        if cnt == k:
            stack = stack + arr[i:]  # k만큼 카운트가 되면, 남은 number를 모두 넣어줌
            break

        stack.append(number[i])

        if stack[-2] < stack[-1]:  # 스택에 넣을 숫자가 기존 스택에 들어있는 숫자 중 가장 위에 있는 숫자보다 크다면,
            while (len(stack) != 1) and (cnt < k) and stack[-2] < stack[-1]:
                # 스와프(가능하게하려면 스택의 원소가 2 이상이어야함. 그래서 len(stack) != 1)
                stack[-2], stack[-1] = stack[-1], stack[-2]
                # 제거
                stack.pop()
                # 카운트
                cnt += 1

    # 예를 들어 99991에서 3개를 제거하면 99가 나와야함. 근데 그냥 stack을 join시키면 제거되는 수가 없기때문에 99991이 출력됨. 이러한 케이스를 해결하기위해 문자열의 개수까지만 출력하도록 만들어줌
    answer = "".join(stack[:length])
    return answer

    # 참고 https://kdgt-programmer.tistory.com/5?category=1121942
