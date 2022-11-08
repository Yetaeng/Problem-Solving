def solution(name):
    target = list(name)
    result = []
    for i in range(len(target)):
        if ord(target[i]) - ord('A') <= 13:
            result.append(ord(target[i]) - ord('A'))
        else:
            result.append(ord('Z')-ord(target[i])+1)

    idx, answer = 0, 0
    while 1:
        answer += result[idx]
        result[idx] = 0
        if sum(result) == 0:  # 더이상 바꿀 문자열이 없다면
            break

        left, right = 1, 1
        # 왼쪽으로 이동했을 때 0이라면, 바꿀 문자열이 아니므로 한칸씩 더 이동
        # 만일 첫번째에서 왼쪽으로 이동하는 경우에는 0자체가 아니므로 반복문을 실행시키지 않는다.
        while result[idx - left] == 0:
            left += 1
        while result[idx + right] == 0:
            right += 1

        # 문자열을 바꾸려고 이동해다녔더라면, left와 rght의 값이 변해있을것
        answer += left if left < right else right
        #
        idx += -left if left < right else right

    return answer

# 출처 https://jgrammer.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%A1%B0%EC%9D%B4%EC%8A%A4%ED%8B%B1
# while문을 구현하는데 위 출처의 도움을 받았다.

# resutl[-2] 를 해도 맨 뒤에서 두번째 문자열을 가져오는데, 문제에서 왼쪽 끝에 다다르면 오른쪽으로 이동한다는 조건을 보고 너무 신경쓴 것 같다..
