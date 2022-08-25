function solution(arr) {
    if (arr.length === 1) return arr;

    let answer = [];
    let num = arr[0];
    answer.push(num);

    for (let i = 1; i < arr.length; i++) {
        if (num !== arr[i]) {
            answer.push(arr[i])
            num = arr[i]
        }
    }

    return answer;
}

function solution2(arr) {
    const answer = arr.filter((v,i) => v !== arr[i+1]);
    
    return answer;
}

const arr = [1,1,3,3,0,1,1];

/**
 * solution result
정확성 테스트
테스트 1 〉	통과 (0.05ms, 29.9MB)
테스트 2 〉	통과 (0.06ms, 29.8MB)
테스트 3 〉	통과 (0.06ms, 30.2MB)
테스트 4 〉	통과 (0.08ms, 30MB)
테스트 5 〉	통과 (0.10ms, 30.1MB)
테스트 6 〉	통과 (0.09ms, 30.3MB)
테스트 7 〉	통과 (0.06ms, 30.1MB)
테스트 8 〉	통과 (0.06ms, 30.1MB)
테스트 9 〉	통과 (0.08ms, 30.1MB)
테스트 10 〉	통과 (0.06ms, 30.1MB)
테스트 11 〉	통과 (0.06ms, 30.2MB)
테스트 12 〉	통과 (0.06ms, 30.2MB)
테스트 13 〉	통과 (0.06ms, 29.8MB)
테스트 14 〉	통과 (0.06ms, 30.1MB)
테스트 15 〉	통과 (0.06ms, 30MB)
테스트 16 〉	통과 (0.14ms, 30MB)
테스트 17 〉	통과 (0.04ms, 30MB)
효율성  테스트
테스트 1 〉	통과 (39.14ms, 75.8MB)
테스트 2 〉	통과 (38.47ms, 75.8MB)
테스트 3 〉	통과 (39.37ms, 76.1MB)
테스트 4 〉	통과 (11.47ms, 75.9MB)
 */

/**
 * solution2 result
정확성 테스트
테스트 1 〉	통과 (0.04ms, 29.8MB)
테스트 2 〉	통과 (0.05ms, 29.8MB)
테스트 3 〉	통과 (0.06ms, 30.2MB)
테스트 4 〉	통과 (0.06ms, 30.1MB)
테스트 5 〉	통과 (0.09ms, 29.9MB)
테스트 6 〉	통과 (0.06ms, 29.7MB)
테스트 7 〉	통과 (0.06ms, 30MB)
테스트 8 〉	통과 (0.06ms, 30.1MB)
테스트 9 〉	통과 (0.13ms, 30MB)
테스트 10 〉	통과 (0.05ms, 30MB)
테스트 11 〉	통과 (0.08ms, 30.1MB)
테스트 12 〉	통과 (0.09ms, 30.1MB)
테스트 13 〉	통과 (0.14ms, 30MB)
테스트 14 〉	통과 (0.06ms, 30.2MB)
테스트 15 〉	통과 (0.06ms, 30MB)
테스트 16 〉	통과 (0.06ms, 30.1MB)
테스트 17 〉	통과 (0.04ms, 30MB)
효율성  테스트
테스트 1 〉	통과 (49.56ms, 76.5MB)
테스트 2 〉	통과 (48.37ms, 75.9MB)
테스트 3 〉	통과 (49.21ms, 75.8MB)
테스트 4 〉	통과 (53.95ms, 75.7MB)
 */