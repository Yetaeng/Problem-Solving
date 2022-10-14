// Lv.2
function solution(numbers, target) {
  let answer = 0;
  dfs(0,0);
  
  function dfs(idx, sum) {
      if (idx === numbers.length) {
          if (sum === target) return answer++;
          return;
      } else {
          dfs(idx+1, sum + numbers[idx]);
          dfs(idx+1, sum - numbers[idx]);
      }
  }
  
  return answer;
}

//