def solution(answers):
    answer = []
    scores = [0, 0, 0]
    student1 = [1,2,3,4,5] # len=5
    student2 = [2,1,2,3,2,4,2,5] # len=8
    student3 = [3,3,1,1,2,2,4,4,5,5] # len=10
    
    for i in range(len(answers)):
        # 1번 수포자의 정답 갯수 구하기
        if answers[i] == student1[i % len(student1)]:
            scores[0] +=1
        if answers[i] == student2[i % len(student2)]:
            scores[1] +=1
        if answers[i] == student3[i % len(student3)]:
            scores[2] +=1
            
    max_score = max(scores)
    
    for i in range(3):
        if scores[i] == max_score:
            answer.append(i+1)
    return answer