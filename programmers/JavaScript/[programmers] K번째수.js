function solution(array, commands) {
  var answer = [];

  for (let i = 0; i < commands.length; i++) {
    let begin = commands[i][0]
    let end = commands[i][1]
    let target = commands[i][2]
    let arr = array.slice(begin - 1, end)
    arr.sort((a, b) => a - b);
    answer.push(arr[target - 1])
  }

  return answer;
}

/**
 * (1)
 * JS의 sort() 메서드에서는 compareFunction이 제공되지 않고, 요소를 문자열로 변환하고 유니코드 코드 포인트 순서로 문자열을 비교하여 정렬된다.
 * 그래서 처음에 단순히 arr.sort()라고만 했다가 특정 케이스에서 실패했었다.
 * (2)
 * slice() 메서드는 어떤 배열의 begin부터 end까지(end 미포함)에 대한 얕은 복사본을 새로운 배열 객체로 반환한다. 원본 배열은 바뀌지 않는다.
 * sort()는 정렬한 배열. 원 배열이 정렬된다. 복사본이 만들어지는 것이 아니다.
 */

 function solution2(numbers) {
  // 문자열을 그대로 연결한 수에서 바꿔 연결한 수를 뺏을 때, 양수면 순서 유지, 음수면 교환함으로써 큰 순서대로 정렬함
  const answer = numbers.map(num => String(num)).sort((a, b) => b+a - (a+b)).join('');

  return answer[0] === '0' ? '0' : answer;
}